# Generated by Django 4.2.2 on 2023-06-28 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0003_pic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pic",
            options={"verbose_name": "Картинка", "verbose_name_plural": "Картинки"},
        ),
        migrations.RemoveField(
            model_name="pic",
            name="title",
        ),
        migrations.AddField(
            model_name="post",
            name="pics",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pics",
                to="places.pic",
                verbose_name="Заголовок",
            ),
            preserve_default=False,
        ),
    ]
