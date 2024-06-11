from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import scrape_coin_data_task
from .models import Job, Task
from .coinmarketcap import CoinMarketCap
import uuid
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
@api_view(['POST'])
def start_scraping(request):
    coins = request.data.get("coins")
    if not all(isinstance(coin, str) for coin in coins):
        return Response({'error': 'Invalid input. Input should be a list of strings.'}, status=400)

    job_id = uuid.uuid4()
    job = Job.objects.create(job_id=job_id, status="PENDING")

    # Start scraping for each coin and store the scraped data
    for coin in coins:
        scraped_data = CoinMarketCap.scrape_coin_data(coin)
        Task.objects.create(job=job, coin=coin, scraped_data=scraped_data)

    return Response({'job_id': job_id}, status=202)

@api_view(['GET'])
def scraping_status(request, job_id):
    try:
        job = Job.objects.get(job_id=job_id)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found.'}, status=404)

    tasks = Task.objects.filter(job=job)
    data = {
        'job_id': job.job_id,
        'tasks': [
            {
                'coin': task.coin,
                'scraped_data': task.scraped_data
            }
            for task in tasks
        ]
    }
    return Response(data)
