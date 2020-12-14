from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command

sched = BackgroundScheduler()


@sched.scheduled_job('cron', hour=9)
def scheduled_job():
    call_command('get_data')


sched.start()
