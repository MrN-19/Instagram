from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class Profile(models.Model):
    GENDER = (("male","مرد"),("woman","زن"),("Prefer to not say","ترجیم میدهم نگویم"))

    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name = "کاربر",related_name="profile")
    biography = models.CharField(max_length=1000,verbose_name="بیوگرافی")
    register_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت نام")
    website = models.URLField(max_length=200,verbose_name="وب سایت",null=True)
    phone_number = models.CharField(max_length=15,verbose_name="موبایل",null=True)
    gender = models.CharField(max_length=150,verbose_name="جنسیت",choices=GENDER,null=True)
    profile_image = models.ImageField(verbose_name="تصویر کاربر",upload_to = "ProfileImages",null=True)

    def clean(self):
        phone = self.phone_number
        if len(str(phone)) != 11:
            raise ValidationError(message="موبایل باید 11 رقم باشد")


    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "پروفایل کاربران"
        verbose_name_plural = "پروفایل کاربران"

class UserLocation(models.Model):
    user = models.ForeignKey(User,verbose_name="کاربر",on_delete=models.CASCADE)
    ip = models.CharField(max_length=100,verbose_name="آی پی")
    country = models.CharField(max_length=150,verbose_name="کشور")
    city = models.CharField(max_length=150,verbose_name="شهر")
    lat = models.FloatField(verbose_name="عرض جغرافیایی")
    long = models.FloatField(verbose_name="طول جغرافیایی")

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "موقعیت مکانی کاربر"
        verbose_name_plural = "موقعیت مکانی کاربر"
        
class FollowersFollowing(models.Model):
    following = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربری که فالو میکند",help_text="Person Who is following",related_name="followinguser")
    followed = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربری که فالو شده است",help_text="Person who followed",related_name="followeduser")
    action_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ انجام")

    def __str__(self):
        show = f"کاربر {self.following.username} کاربر {self.followed.username} را دنبال میکند"
        return show
    class Meta:
        verbose_name = "فالوور ها"
        verbose_name_plural = "فالوور ها"

class BlockUser(models.Model):
    user_is_blocking = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربری که بلاک کرده",help_text="User who is blocking",related_name="userblocking")
    user_is_blocked = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر بلاک شده",help_text="Person Who blocked",related_name="userblocked")
    action_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ انجام")

    def __str__(self):
        show = f"کاربر {self.user_is_blocking} کاربر {self.user_is_blocked} را بلاک کرده است"
        return show
    class Meta:
        verbose_name = "کاربران بلاک شده"
        verbose_name_plural = "کاربران بلاک شده"
    
class SearchHostory(models.Model):
    user = models.ForeignKey(User,verbose_name="کاربر",on_delete=models.CASCADE)
    text_searched = models.CharField(max_length=150,verbose_name="متن جستجو شده")
    search_date = models.DateTimeField(verbose_name="تاریخ جستجو",auto_now=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "تاریخچه جستجو"
        verbose_name_plural = "تاریخچه جستجو"

class AccountSetting(models.Model):
    user = models.OneToOneField(User,verbose_name="کاربر",on_delete=models.CASCADE,related_name="accountsetting")
    is_private_page = models.BooleanField(default=False,verbose_name="آیا پیج خصوصی است ؟")
    show_activity_status = models.BooleanField(default=False,verbose_name="نشان دادن وضیعت فعال بودن")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "تنظیمات حساب"
        verbose_name_plural = "تنظیمات حساب"

class TwoFactorAuthentication(models.Model):
    user = models.ForeignKey(User,verbose_name="کاربر",on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False,verbose_name="فعال است ؟")
    text_message = models.CharField(max_length=20,verbose_name="کد")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "ورود دو مرحله ای"
        verbose_name_plural = "ورود دو مرحله ای"
        


