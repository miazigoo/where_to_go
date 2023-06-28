from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = RichTextUploadingField('Полное описание')
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    point_lon = models.FloatField(verbose_name="Долгота точки", blank=True, null=True)
    point_lat = models.FloatField(verbose_name="Широта точки", blank=True, null=True)
    slug = models.SlugField('Название в виде url', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Pic(models.Model):
    numb = models.IntegerField(verbose_name="Порядковый номер:")
    title = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Заголовок", related_name='pics')
    picturies = models.ImageField(verbose_name="Картинка", upload_to='img', blank=True)

    def __str__(self):
        return f'{self.numb} {self.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    @property
    def photo_preview(self):
        if self.picturies:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.picturies.url))
        return ""


