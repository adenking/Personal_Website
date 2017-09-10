from django.db import models


# Create your models here.
class BlogEntry(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.blog_title
