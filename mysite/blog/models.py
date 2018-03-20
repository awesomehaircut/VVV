from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class BlogPost(models.Model):
    """
    Hopefully this class is all I need for a blog post.
    """
    title = models.CharField(max_length=70)
    # date = models.DateField()
    content = models.TextField()
    ispublished = models.BooleanField()
    tags = [models.CharField(max_length=70)]
    datepulished = models.DateTimeField(default=timezone.now())
    lastedit = models.DateTimeField(auto_now=True)

    def create(self):
        self.lastedit = datetime.now()
        if len(self.title) < 1:
            self.title = input("Title: ")
        if len(self.content) < 1:
            self.content = input("Start typing:")
        self.tags = input("Tags?").split(',')

    def __str__(self):
        return self.title  
