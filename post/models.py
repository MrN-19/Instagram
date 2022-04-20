from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from utilities.utilities import generate_code
class LocationTag(models.Model):
    pass
class HashTag(models.Model):
    pass
class AllowedExtensions(models.Model):
    file_allowed = models.CharField(max_length=20,verbose_name="فایل مجاز")

    def __str__(self):
        return self.file_allowed
    class Meta:
        verbose_name = "فرمت های مجاز فایل ها"
        verbose_name_plural = "فرمت های مجاز فایل ها"

class Post(models.Model):

    allowed_file_extensions = [ext.file_allowed for ext in AllowedExtensions.objects.all()]

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "کاربر",related_name="userposts")
    code = models.CharField(null=True,blank=True,max_length=20,verbose_name="کد منحصر به فرد",help_text="ای فیلد را پر نکنید به صورت خودکار پر میشود")
    caption = models.TextField(verbose_name="متن")
    location_tag = models.ForeignKey(LocationTag,on_delete=models.CASCADE,verbose_name="مکان",null=True,blank=True)
    hashtags = models.ForeignKey(HashTag,on_delete=models.CASCADE,verbose_name="برچسب",null=True,blank=True)
    is_multi_slide = models.BooleanField(default=False,verbose_name="آیا چند اسلایدی است ؟")
    image_or_video = models.FileField(upload_to="PostImages"
    ,verbose_name="فایل چند رسانه ای",validators=[FileExtensionValidator(allowed_extensions=allowed_file_extensions,message="فرمت فایل وارد شده مجاز نیست")])
    tagged_users = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربران تگ شده",null=True,blank=True,related_name="usertagged")
    publish_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ انتشار")

    def __str__(self):
        return self.user.username
    def save(self,*args,**kwargs):
        self.code = generate_code(20)
        super(Post,self).save(*args,**kwargs)
        
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

class PostLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "کاربر",related_name="userpostlike")
    post = models.ForeignKey(Post,verbose_name="پست",on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "پسند پست"
        verbose_name_plural = "پسند پست"

class PostComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "کاربر")
    is_header = models.BooleanField(default=False,verbose_name="آیا سر گروه است ؟")
    header = models.ForeignKey("self",verbose_name="سر گروه",on_delete=models.CASCADE,null=True,blank=True)
    post = models.ForeignKey(Post,verbose_name="پست",on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="نظر")
    commented_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "نظرات پست"
        verbose_name_plural = "نظرات پست"
class CommentLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "کاربر")
    comment = models.ForeignKey(PostComment,verbose_name="نظر",on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "پسند نظرات"
        verbose_name_plural = "پسند نظرات"

class PostSave(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="پست")
    saved_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "ذخیره پست"
        verbose_name_plural = "ذخیره پست"


