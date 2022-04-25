from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET,require_http_methods,require_POST
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.models import Post
from .models import FollowersFollowing,BlockUser
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
    if post_code and follow_un_follow_type:
        result = action_follow_un_follow(post_code=post_code,follow_un_follow_type=follow_un_follow_type,user=request.user)
        if result[0]:
            return JsonResponse({
                "status" : True,"message" : "Success 200","text" : result[1]
            })
        return JsonResponse({
            "status" : True,"message" : "403 Bad Request","text" : result[1]
        },status = 403)
    return JsonResponse({
        "status" : False,"message" : "403 Bad Request","text" : "خطا در انجام عملیات"
    },status = 403)



@login_required(login_url="account:login")
@require_POST
def block_user_by_post(request):
    post_code = request.POST.get("code")
    post_code = clean_text(post_code)
    if post_code:
        user_will_block = Post.objects.filter(code = post_code).first().user
        BlockUser.objects.create(
            user_is_blocking = request.user,
            user_is_blocked = user_will_block,
        )
        return JsonResponse({
            "status" : True,"message" : "Success 200","text" : "عملیات با موفقیت انجام شد"
        })
    return JsonResponse({
        "status" : False,"message" : "403 Bad Request","text" : "خطا در انجام عملیات"
    },status = 403)