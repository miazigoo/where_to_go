# Generated by Django 4.2.2 on 2023-06-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0007_post_point_lat_post_point_lon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="point_lat",
            field=models.FloatField(blank=True, null=True, verbose_name="Широта точки"),
        ),
        migrations.AlterField(
            model_name="post",
            name="point_lon",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Долгота точки"
            ),
        ),
    ]
