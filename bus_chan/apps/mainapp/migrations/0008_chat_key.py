# Generated by Django 3.0.6 on 2020-05-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200525_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='key',
            field=models.CharField(blank=True, max_length=80, verbose_name='Приватный ключ'),
        ),
    ]