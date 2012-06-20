from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class article(models.Model):
    title=models.CharField(max_length=30)
    
    
class FileUpload(models.Model):
    files=models.FileField(upload_to='files')
    
    
class SaveCSV(models.Model):
    user=models.ForeignKey(User)
    title=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    city=models.CharField(max_length=30)        