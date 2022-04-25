from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET,require_http_methods,require_POST
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.models import Post
from .models import FollowersFollowing
from utilities.utilities import clean_text

def action_follow_un_follow(post_code:str,follow_un_follow_type:str,user:User) -> tuple:
    post = Post.objects.filter(code = post_code).first()
    if post:
        if follow_un_follow_type == "follow":
            FollowersFollowing.objects.create(following = user,followed = post.user)
            return True,f"کاربر {post.user} فالو شد"
        elif follow_un_follow_type == "unfollow":
            follow_unfollow = FollowersFollowing.objects.filter(following = user,followed = post.user).first()
            if follow_unfollow:
                follow_unfollow.delete()
                return True,f"کاربر {post.user} آنفالو شد"
            return False,"خطا در انجام عملیات" 
        else:
            return False,"خطا در انجام عملیات"
    return False,"خطا در انجام عملیات"

@login_required(login_url="account:login")
@require_POST
def follow_unfollow_user(request):
    post_code = request.POST.get("code")
    post_code = clean_text(post_code)
    follow_un_follow_type = str(request.POST.get("type"))
    result = action_follow_un_follow(post_code=post_code,follow_un_follow_type=follow_un_follow_type,user=request.user)
    if result[0]:
        return JsonResponse({
            "status" : True,"message" : "Success 200","text" : result[1]
        })
    return JsonResponse({
        "status" : True,"message" : "403 Bad Request","text" : result[1]
    },status = 403)

    

