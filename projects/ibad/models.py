from distutils.command.upload import upload

from django.db import models
from tinymce import models as tinymce_models




# Create your models here.
class Post(models.Model):
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=200)
    slug=models.SlugField()
    intro=models.TextField()
    body=tinymce_models.HTMLField()
    date_added=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='images/',null=True)


class Form(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    reason=models.TextField()    