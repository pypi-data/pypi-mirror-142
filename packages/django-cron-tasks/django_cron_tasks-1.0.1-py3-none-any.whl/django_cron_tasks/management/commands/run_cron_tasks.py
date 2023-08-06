import importlib
import io
import sys
import traceback

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from django_cron_tasks import models


class Command(BaseCommand):
    help = 'Runs background tasks.'

    def handle(self, *args, **options):

        for task in getattr(settings, 'DJANGO_CRON_TASKS', []):
            latest_run = models.TaskResult.objects.filter(name=task['task']).order_by('started_at').last()
            # TODO: Support crontab like syntax too!
            if not latest_run or latest_run.started_at + task['schedule'] < timezone.now():
                # TODO: Make some kind of locking mechanism, so that the task is not started twice!
                # Get function
                task_splitted = task['task'].split('.')
                module_path = '.'.join(task_splitted[0:-1])
                func_name = task_splitted[-1]
                module = importlib.import_module(module_path)
                func = getattr(module, func_name)

                # Create a new entry to database
                result = models.TaskResult.objects.create(
                    name=task['task'],
                )

                # Run it
                func_output = io.StringIO()
                default_stdout = sys.stdout
                default_stderr = sys.stderr
                sys.stdout = func_output
                sys.stderr = func_output
                try:
                    func()
                except Exception as err:
                    # Mark task failed
                    result.finished_at = timezone.now()
                    result.success = False
                    result.output = func_output.getvalue() + traceback.format_exc()
                    result.save(update_fields=['finished_at', 'success', 'output'])
                    # Try the next task
                    continue
                finally:
                    sys.stdout = default_stdout
                    sys.stderr = default_stderr

                # Mark task finished successfully
                result.finished_at = timezone.now()
                result.success = True
                result.output = func_output.getvalue()
                result.save(update_fields=['finished_at', 'success', 'output'])
