from django.db import models


class News(models.Model):
    news_id= models.IntegerField(primary_key=True, auto_created=True)
    author = models.CharField(max_length=250)
    news_score = models.IntegerField(default=0)
    news_title = models.CharField(max_length=250)
    news_type = models.CharField(max_length=250)
    news_url = models.URLField()
    news_time = models.DateTimeField(auto_now=True)
    is_created = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.news_title