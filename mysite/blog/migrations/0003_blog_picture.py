# Generated by Django 3.0.7 on 2020-06-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
