# Generated by Django 2.2.5 on 2020-06-27 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')),
                ('description', models.TextField(verbose_name='محتوا')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='عکس مقاله')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت')),
            ],
        ),
    ]
