from datetime import date, timedelta
from celery.task import Task, PeriodicTask
from about_us.models import Person


class CheckPersonTask(Task):
    """
    A task that determines if a person is 21 years of age or older.
    """
    def run(self, person_id, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info("Running checking task for person %s" % person_id)
        return True

class FullNameTask(PeriodicTask):
    """
    A periodic task that concatenates fields to form a person's full name.
    """
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info("Running periodic task.")
        return True