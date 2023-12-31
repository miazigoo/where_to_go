# Generated by Django 4.2.2 on 2023-06-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0008_alter_post_point_lat_alter_post_point_lon"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                blank=True,
                max_length=200,
                null=True,
                verbose_name="Название в виде url",
            ),
        ),
    ]
