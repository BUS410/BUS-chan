# Generated by Django 3.0.6 on 2020-05-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200507_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Категория чата'),
        ),
    ]
