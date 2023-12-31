from django.db import models
from tinymce.models import HTMLField
from django.utils.safestring import mark_safe

from where_to_go import settings


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    short_description = models.TextField('Короткое описание')
    long_description = HTMLField('Полное описание')
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    point_lon = models.FloatField(verbose_name="Долгота точки", blank=True, null=True)
    point_lat = models.FloatField(verbose_name="Широта точки", blank=True, null=True)
    slug = models.SlugField('Название в виде url', max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Pic(models.Model):
    sequence_number = models.IntegerField(verbose_name="Порядковый номер:", blank=True, null=True)
    title = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Заголовок", related_name='pics')
    image = models.ImageField(verbose_name="Картинка", upload_to='img', blank=True)

    def __str__(self):
        return f'{self.sequence_number} {self.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['sequence_number']

    @property
    def photo_preview(self):
        if self.image:
            return mark_safe('<img src="{}" height="200" />'.format(self.image.url))
        return ""

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)
