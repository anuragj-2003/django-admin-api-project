from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coin_scraper_project.settings')

app = Celery('coin_scraper_project_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['coin_scraper'])

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
