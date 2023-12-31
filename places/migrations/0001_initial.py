# Generated by Django 4.2.2 on 2023-06-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                ("description_short", models.TextField(verbose_name="Текст")),
                ("description_long", models.TextField(verbose_name="Текст")),
                ("lat", models.FloatField(verbose_name="Широта")),
                ("lon", models.FloatField(verbose_name="Долгота")),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
    ]
