# Generated by Django 5.1.1 on 2024-09-19 13:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
