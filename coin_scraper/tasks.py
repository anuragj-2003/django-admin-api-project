from celery import shared_task
from .models import Job, Task
from .coinmarketcap import CoinMarketCap

@shared_task
def scrape_coin_data_task(job_id, coins):
    job = Job.objects.get(job_id=job_id)
    job.status = 'IN_PROGRESS'
    job.save()
    
    for coin in coins:
        data = CoinMarketCap.scrape_coin_data(coin)
        Task.objects.create(job=job, coin=coin, scraped_data=data)
    
    job.status = 'COMPLETED'
    job.save()