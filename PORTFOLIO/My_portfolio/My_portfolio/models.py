from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    technical_skills = models.TextField()
    # Add more fields as needed
