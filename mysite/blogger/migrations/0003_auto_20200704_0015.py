# Generated by Django 3.0.7 on 2020-07-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_auto_20200704_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='user',
        ),
    ]