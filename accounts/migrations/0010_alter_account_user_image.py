# Generated by Django 4.2.5 on 2023-10-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_account_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_image',
            field=models.ImageField(blank=True, default='profile_picture/propic_cwuy8f', null=True, upload_to='profile_picture'),
        ),
    ]
