from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=250)
    is_upcoming = models.BooleanField(default=True)
    thumbnail = models.FileField(upload_to="images")
    timestamp = models.DateTimeField()
    venue = models.CharField(max_length=250, default="To Be Decided")
    description = models.TextField()

    def __str__(self):
        return self.title
    
class EventImages(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images")

    def __str__(self):
        return self.event.title
    
    class Meta:
        verbose_name_plural = "Event Images"
    

class Member(models.Model):
    name = models.CharField(max_length=205)
    designation = models.CharField(max_length=205)
    bio = models.TextField()
    picture = models.FileField(upload_to="team")

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.FileField(upload_to="blogs")
    author = models.CharField(max_length=205)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Query(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
