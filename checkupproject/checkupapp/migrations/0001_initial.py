# Generated by Django 3.0 on 2021-05-06 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=1)),
                ('weight', models.IntegerField(default=1)),
                ('height', models.IntegerField(default=1)),
                ('tel', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=255, unique=True)),
                ('userimage', models.ImageField(blank=True, null=True, upload_to='image')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HT', models.BooleanField(default=False)),
                ('DM', models.BooleanField(default=False)),
                ('DLP', models.BooleanField(default=False)),
                ('hepatitis', models.BooleanField(default=False)),
                ('chronic_hepatitis', models.BooleanField(default=False)),
                ('osteoporosis', models.BooleanField(default=False)),
                ('allergy', models.BooleanField(default=False)),
                ('CVS', models.BooleanField(default=False)),
                ('renal_stone', models.BooleanField(default=False)),
                ('cancer', models.BooleanField(default=False)),
                ('CA_breast', models.BooleanField(default=False)),
                ('CA_ovary', models.BooleanField(default=False)),
                ('CA_cervix', models.BooleanField(default=False)),
                ('CA_GI', models.BooleanField(default=False)),
                ('CA_liver', models.BooleanField(default=False)),
                ('CA_pancreas', models.BooleanField(default=False)),
                ('CA_others', models.BooleanField(default=False)),
                ('CA_prostate', models.BooleanField(default=False)),
                ('userdetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkupapp.UserDetail')),
            ],
        ),
    ]
