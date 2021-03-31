from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.title + ' | ' +str(self.author)

    def get_absolute_url(self):
        return reverse('post_details', args=(str(self.id)))
        #return reverse('home)
    
    
