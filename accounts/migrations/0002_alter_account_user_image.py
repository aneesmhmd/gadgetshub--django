# Generated by Django 4.1.7 on 2023-03-15 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_image',
            field=models.ImageField(blank=True, default='static/images/logo/propic.png', null=True, upload_to='profile_picture'),
        ),
    ]