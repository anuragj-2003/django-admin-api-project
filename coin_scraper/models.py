from django.db import models

class Job(models.Model):
    job_id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=20, choices=[("PENDING", "Pending"), ("IN_PROGRESS", "In Progress"), ("COMPLETED", "Completed")])

class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    coin = models.CharField(max_length=100)
    scraped_data = models.JSONField()
