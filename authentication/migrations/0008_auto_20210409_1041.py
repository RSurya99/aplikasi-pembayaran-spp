# Generated by Django 2.2.12 on 2021-04-09 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20210403_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='profile-picture-default.jpg', null=True, upload_to='profile/'),
        ),
    ]
