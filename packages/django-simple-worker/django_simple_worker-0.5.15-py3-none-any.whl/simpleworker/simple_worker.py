import logging
import pickle
import signal
from datetime import timedelta
from time import sleep
from typing import Optional, List

from django.db import transaction
from django.utils import timezone

from simpleworker.models import Task, TaskResult
from simpleworker.simple_task import SimpleTask

logger = logging.getLogger(__name__)


class SimpleWorker:
    queues: Optional[List] = None
    exit = False
    errors_in_a_row = 0
    max_errors_in_a_row = 10

    def __init__(self, queues: Optional[List] = None):
        if queues is not None and len(queues) > 0:
            self.queues = queues
        signal.signal(signal.SIGINT, self.set_exit)
        signal.signal(signal.SIGTERM, self.set_exit)

    def set_exit(self, signum, frame):
        self.exit = True
        logger.info(f'Exiting on signal {signum}')
        exit(0)

    def handle_task(self, task: Task):
        if self.errors_in_a_row > self.max_errors_in_a_row:
            logger.info(f'Encountered {self.errors_in_a_row} errors in a row. This may indicate worker problems. Exiting with error code 0.')
            exit(0)

        task_id = task.id
        task_name = task.name
        logger.info(f'Starting processing task {task_name} id {task_id}')
        max_retries = None
        try:
            simple_task: SimpleTask = pickle.loads(task.payload)
            max_retries = simple_task.max_retries
            simple_task.handle()
            TaskResult.add(task)
            task.delete()
            self.errors_in_a_row = 0
        except Exception as ex:
            self.errors_in_a_row += 1

            logger.exception(ex)
            if max_retries is not None and max_retries >= task.tries:
                try:
                    from sentry_sdk import capture_exception
                    capture_exception(ex)
                except Exception as ex:
                    logger.exception(ex)
                logger.warning(f'Error occured when processing task id {task_id}. Task will not be retried, max_retries exceeded')
                TaskResult.add(task, error=str(ex))
                task.delete()
                return

            next_try = timezone.now() + timedelta(minutes=1)
            logger.warning(f'Error occured when processing task id {task_id}. Will be retried at {next_try}')
            task.tries += 1
            task.next_try = next_try
            task.last_error = str(ex)
            task.save()
        logger.info(f'Processing task {task_name} id {task_id} finished')

    def run(self):
        logger.info('Worker starting')

        if self.queues is not None and len(self.queues) > 0:
            logger.info(f"Processing queues {','.join(self.queues)}")
        else:
            logger.info('All queues will be processed')

        db = 'worker'
        while not self.exit:
            with transaction.atomic(using=db):
                task = Task.get_next(db, self.queues)
                if task is None:
                    logger.debug('No tasks to process')
                    sleep(5)
                    continue
                else:
                    self.handle_task(task)

        logger.info('Worker exiting')
