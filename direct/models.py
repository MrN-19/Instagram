from django.db import models
from django.contrib.auth.models import User
class DirectMessage(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="ارسال کننده",related_name="usersneder")
    reciver = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="دریافت کننده",related_name="userreciver")
    send_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ارسال")
    message_text = models.TextField(null=True)
    media = models.FileField(verbose_name="فایل",upload_to="DirectMedias",null=True,blank=True)
    seen_state = models.BooleanField(default=False,verbose_name="مشاهده شده ؟")
    send_state = models.BooleanField(default=False,verbose_name="ارسال شده ؟")

    def __str__(self):
        return f"ارسال کننده {self.sender.username}" + " " + "دریافت کننده" + self.reciver.username

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    