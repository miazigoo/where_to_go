from django.db import models
from tinymce.models import HTMLField
from django.utils.safestring import mark_safe

from where_to_go import settings
from uuid import uuid4
from pytils.translit import slugify


def unique_slugify(instance, slug):
    """
    Генератор уникальных SLUG для моделей, в случае существования такого SLUG.
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Полное описание')
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    point_lon = models.FloatField(verbose_name="Долгота точки", blank=True, null=True)
    point_lat = models.FloatField(verbose_name="Широта точки", blank=True, null=True)
    slug = models.SlugField('Название в виде url', max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Pic(models.Model):
    numb = models.IntegerField(verbose_name="Порядковый номер:", blank=True, null=True)
    title = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Заголовок", related_name='pics')
    picturies = models.ImageField(verbose_name="Картинка", upload_to='img', blank=True)

    def __str__(self):
        return f'{self.numb} {self.title}'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.numb:
            self.numb = self.pk
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['numb']

    @property
    def photo_preview(self):
        if self.picturies:
            return mark_safe('<img src="{}" height="200" />'.format(self.picturies.url))
        return ""

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.picturies.url)
