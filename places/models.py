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


class Pic(models.Model):
    numb = models.IntegerField(verbose_name="Порядковый номер:")
    title = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Заголовок", related_name='posts')
    picturies = models.ImageField(verbose_name="Картинка", upload_to='img', blank=True)

    def __str__(self):
        return f'{self.numb} {self.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
