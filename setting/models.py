from django.db import models
from django.contrib.auth.models import User

class AppInfo(models.Model):
    site_name = models.CharField(max_length=150,verbose_name="نام سایت شما")
    logo = models.FileField(upload_to="SiteMedias",verbose_name="فایل لوگو")
    domainname = models.URLField(verbose_name="آدرس سایت")

    def __str__(self):
        return self.site_name
    class Meta:
        verbose_name = "اطلاعات سایت"
        verbose_name_plural = "اطلاعات سایت"

class UserRequestRule(models.Model):

    LIMIT_TYPE = (("block for ever","محدودیت همیشگی"),("block one week","محدودیت یک هفته ای"),("block one month","محدودیت یک ماه")
    ,("block one year","محدودیت یک سال"),("block a day","محدودیت یک روزه"),("block one hour","محدودیت یک روزه"))

    REQUEST_ADDRESS = (("likes","لایک"),("comment","نظر"),("follow","فالو"),("unfollow","آنفالو"))

    request_address = models.CharField(max_length=200,verbose_name="آدرس ارسال درخواست",choices=REQUEST_ADDRESS)
    request_count = models.SmallIntegerField(default=0,verbose_name="تعداد درخواست")
    limit_type = models.CharField(max_length=200,verbose_name="نوع محدودیت",choices=LIMIT_TYPE)

    def __str__(self):
        return "قوانین محدودیت" + self.request_address

    class Meta:
        verbose_name = "قوانین محدودیت"
        verbose_name_plural = "قوانین محدودیت"

