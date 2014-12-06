import datetime
from django.db import models
from django.utils import timezone

class Blog_Post(models.Model): 
    def __str__(self): 
        return self.title_text
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    post_photo = models.ImageField(upload_to="blog/photos")
    post_content_text = models.TextField()

