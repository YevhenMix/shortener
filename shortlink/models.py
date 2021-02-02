from django.db import models


class Url(models.Model):
    long_url = models.URLField(verbose_name='Полная ссылка')
    short_url = models.CharField(max_length=200, verbose_name='Короткая ссылка')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.long_url
