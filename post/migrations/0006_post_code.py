# Generated by Django 4.0.4 on 2022-04-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_postsave'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code',
            field=models.CharField(help_text='ای فیلد را پر نکنید به صورت خودکار پر میشود', max_length=20, null=True, verbose_name='کد منحصر به فرد'),
        ),
    ]
