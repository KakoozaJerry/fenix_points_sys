# Generated by Django 2.2.1 on 2019-05-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20190526_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='points',
            name='password',
            field=models.CharField(default='123', max_length=30),
        ),
    ]
