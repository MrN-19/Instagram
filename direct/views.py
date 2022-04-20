from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import DirectMessage
from setting.models import AppInfo
from django.contrib import messages

def check_user_exists(usernames:list) -> bool:
    db_users = User.objects.all()
    res = True
    for i in usernames:
        if not User.objects.filter(username = i).first() in db_users:
            res = False
    return res


@login_required(login_url="account:login")
def share_post_direct(request):
    postid = request.POST.get("postid")
    post = Post.objects.filter(code = postid).first()
    if post:
        usernames = request.POST.getlist("users[]")
        app_domain = AppInfo.objects.last().domainname
        if check_user_exists(usernames=usernames):
            for i in usernames:
                user = User.objects.filter(username = i).first()
                DirectMessage.objects.create(
                    sender = request.user,
                    reciver = user,
                    message_text = app_domain + "post/" + post.code,
                    send_state = True
                )
            messages.success(request,"پیام شما با موفقیت ارسال شد",extra_tags="success")
            return JsonResponse({
                "status" : True,"messages" : "Success 200","text" : "ارسال شد"
            })           
    return JsonResponse({
        "status" : False,"message" : "Not Found 404",
        "text" : "خطا در انجام عملیات"
    },status = 404)