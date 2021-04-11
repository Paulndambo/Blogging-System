from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")

    class Meta:
        verbose_name_plural = ("Categories")

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField() 
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profiles/")
    website = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile", args=(str(self.id)))
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    blog_image = models.ImageField(blank=True, null=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=200)
    snippet = models.CharField(max_length=200, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()    

    def __str__(self):
        return self.title + ' | ' +str(self.author)

    class Meta:
        verbose_name_plural = ("Blog Posts")

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



"""
    def get_absolute_url(self):
        return reverse('post_details', args=(str(self.id)))
        #return reverse('home)
"""
    
