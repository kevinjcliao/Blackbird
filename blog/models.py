import datetime
from django.db import models
from django.utils import timezone

class Title(models.Model): 
    def __str__(self): 
        return self.title_text
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Post_Content(models.Model): 
    def __str__(self): 
        return self.post_content_text
    title = models.ForeignKey(Title)
    post_content_text = models.TextField()
