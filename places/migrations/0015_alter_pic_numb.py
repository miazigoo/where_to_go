# Generated by Django 4.2.2 on 2023-07-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0014_alter_pic_numb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pic",
            name="numb",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Порядковый номер:"
            ),
        ),
    ]