from django.db import models
from django.contrib.auth.models import User

# class Sotry(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
#     publish_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ انتشار")
#     media = models.FileField(upload_to="StoryM