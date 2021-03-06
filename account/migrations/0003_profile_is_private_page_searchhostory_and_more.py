# Generated by Django 4.0.4 on 2022-04-16 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_profile_gender_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_private_page',
            field=models.BooleanField(default=False, verbose_name='آیا پیج خصوصی است ؟'),
        ),
        migrations.CreateModel(
            name='SearchHostory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_searched', models.CharField(max_length=150, verbose_name='متن جستجو شده')),
                ('search_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ جستجو')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تاریخچه جستجو',
                'verbose_name_plural': 'تاریخچه جستجو',
            },
        ),
        migrations.CreateModel(
            name='FollowersFollowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ انجام')),
                ('followed', models.ForeignKey(help_text='Person who followed', on_delete=django.db.models.deletion.CASCADE, related_name='followeduser', to=settings.AUTH_USER_MODEL, verbose_name='کاربری که فالو شده است')),
                ('following', models.ForeignKey(help_text='Person Who is following', on_delete=django.db.models.deletion.CASCADE, related_name='followinguser', to=settings.AUTH_USER_MODEL, verbose_name='کاربری که فالو میکند')),
            ],
            options={
                'verbose_name': 'فالوور ها',
                'verbose_name_plural': 'فالوور ها',
            },
        ),
        migrations.CreateModel(
            name='BlockUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ انجام')),
                ('user_is_blocked', models.ForeignKey(help_text='Person Who blocked', on_delete=django.db.models.deletion.CASCADE, related_name='userblocked', to=settings.AUTH_USER_MODEL, verbose_name='کاربر بلاک شده')),
                ('user_is_blocking', models.ForeignKey(help_text='User who is blocking', on_delete=django.db.models.deletion.CASCADE, related_name='userblocking', to=settings.AUTH_USER_MODEL, verbose_name='کاربری که بلاک کرده')),
            ],
            options={
                'verbose_name': 'کاربران بلاک شده',
                'verbose_name_plural': 'کاربران بلاک شده',
            },
        ),
    ]
