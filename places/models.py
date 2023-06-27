from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = RichTextUploadingField('Полное описание')
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
