# Generated by Django 3.0 on 2021-05-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkupapp', '0003_auto_20210506_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
