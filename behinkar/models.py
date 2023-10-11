from django.db import models
from datetime import datetime

# Create your models here.
class adtitle(models.Model):
    company_name=models.CharField(max_length=150)
    state=models.CharField(max_length=50)
    Description=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True,auto_now=False)


    def __str__(self):
        return self.company_name





