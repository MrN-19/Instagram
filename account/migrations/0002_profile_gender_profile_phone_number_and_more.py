# Generated by Django 4.0.4 on 2022-04-16 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'مرد'), ('woman', 'زن'), ('Prefer to not say', 'ترجیم میدهم نگویم')], max_length=150, null=True, verbose_name='جنسیت'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='موبایل'),
        ),
        migrations.AddField(
            model_name='profile',
            name='register_date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت نام'),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(null=True, verbose_name='وب سایت'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='آی پی')),
                ('country', models.CharField(max_length=150, verbose_name='کشور')),
                ('city', models.CharField(max_length=150, verbose_name='شهر')),
                ('lat', models.FloatField(verbose_name='عرض جغرافیایی')),
                ('long', models.FloatField(verbose_name='طول جغرافیایی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'موقعیت مکانی کاربر',
                'verbose_name_plural': 'موقعیت مکانی کاربر',
            },
        ),
    ]