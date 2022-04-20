from django.db import models

class AppInfo(models.Model):
    site_name = models.CharField(max_length=150,verbose_name="نام سایت شما")
    logo = models.FileField(upload_to="SiteMedias",verbose_name="فایل لوگو")
    domainname = models.URLField(verbose_name="آدرس سایت")

    def __str__(self):
        return self.site_name
    class Meta:
        verbose_name = "اطلاعات سایت"
        verbose_name_plural = "اطلاعات سایت"