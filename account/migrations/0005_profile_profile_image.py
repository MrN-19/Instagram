# Generated by Django 4.0.4 on 2022-04-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_profile_is_private_page_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='ProfileImages', verbose_name='تصویر کاربر'),
        ),
    ]
