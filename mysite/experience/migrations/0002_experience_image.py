# Generated by Django 4.2.5 on 2024-02-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.FileField(blank=True, upload_to='experience_images/'),
        ),
    ]
