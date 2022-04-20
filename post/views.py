from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST,require_http_methods

from .models import Post, PostComment, PostLike, PostSave
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from account.models import FollowersFollowing
from django.core.serializers import serialize
from django.contrib.auth.models import User
def check_user_can_see_post(post,request):
    if post.user.accountsetting.is_private_page == False or post.user.followeduser.filter(following = request.user,followe = post.user).exists():
        return True
    return False

@require_POST
@login_required(login_url="account:login")
def like_post(request):
    data = request.POST
    post_code = data.get("code")
    print(post_code)
    post = Post.objects.filter(code = post_code).first()
    try:
        if post:
            if check_user_can_see_post(post,request):
                post_like = PostLike.objects.filter(user_id = request.user.id,post = post).first()
                like = False
                if not post_like:
                    PostLike.objects.create(
                        user_id = request.user.id,
                        post = post,
                    )
                    like = True
                else:
                    like = False
                    post_like.delete()
                return JsonResponse({
                    "status" : True,
                    "message" : "Success 200",
                    "text" : "انجام شد",
                    "like" : like
                },status = 200)
            else:
                return JsonResponse({
                    "status" : False,
                    "message" : "Bad Request 403",
                    "text" : "خطا در انجام عملیات"
                },status = 403)
        else:
            return JsonResponse({
                "status" : False,
                "message" : "Bad Request 403",
                "text" : "خطا در انجام عملیات"
            },status = 403)
    except Exception as e:
        print(e)
        return JsonResponse({
            "status" : False,
            "message" : "Bad Request 403",
            "text" : "خطا در انجام عملیات"
        },status = 403)
@require_POST
@login_required(login_url="account:login")
def save_post(request):
    data = request.POST
    post_code = data.get("code")
    post = Post.objects.filter(code = post_code).first()
    try:
        if post:
            post_save = PostSave.objects.filter(user = request.user,post = post).first()
            saved = False
            if not post_save:
                PostSave.objects.create(
                    user = request.user,post = post
                )
                saved = True
            else:
                post_save.delete()
            return JsonResponse({
                "status" : True,"message" : "Success 200","text" : "انجام شد",
                "saved" : saved
            },status = 200)
    except:
        return JsonResponse({
            "status" : False,
            "message" : "Bad Request 403",
            "text" : "خطا در انجام عملیات"
        },status = 403)

@login_required(login_url="account:login")
@require_GET
def get_users_to_share_post(request):
    try:
        current_user_followings = FollowersFollowing.objects.filter(following = request.user)
        ready_data = []
        for i in current_user_followings:
            ready_data.append(
                i.followed.username
            )
        data = {
            "status" : True,"message" : "Success 200",
            "data" : ready_data
        }
        return JsonResponse(data,status = 200)
    except Exception as e:
        print(e)
        return JsonResponse({
            "status" : False,
            "message" : "Bad Request 403",
            "text" : "خطا در انجام عملیات"
        },status = 403)

@login_required(login_url="account:login")
@require_GET
def get_picture_by_username(request,username):
    try:
        user_picture = User.objects.filter(username = username).first().profile.profile_image.url
        if user_picture:
            return JsonResponse({
                "picture" : user_picture
            })
        else:
            return JsonResponse({
                "status" : False,
                "message" : "Bad Request 403",
                "text" : "خطا در انجام عملیات"
            },status = 403) 
    except:
        return JsonResponse({
            "status" : False,
            "message" : "Bad Request 403",
            "text" : "خطا در انجام عملیات"
        },status = 403)

@login_required(login_url="account:login")
@require_GET
def set_comment(request,text,postid,header):
    try:
        post = Post.objects.filter(code = postid).first()
        if post:
            if header == 0:
                PostComment.objects.create(
                    user = request.user,
                    post = post,
                    comment = text,
                    is_header = True,
                    header = None
                )
            else:
                header_comment = PostComment.objects.filter(id = header).first()
                if header_comment:
                    PostComment.objects.create(
                        user = request.user,
                        post = post,
                        comment = text,
                        is_header = header_comment
                    )
                else:
                    return JsonResponse({
                        "status" : False,
                        "message" : "Not Found 404",
                        "text" : "خطا در انجام عملیات"
                    },status = 404)
        return JsonResponse({
            "status" : True,
            "message" : "Success 200",
            "text" : "نظر شما ثبت شد"
        },status = 200)     
    except:
        return JsonResponse({
            "status" : False,
            "message" : "Bad Request 403",
            "text" : "خطا در انجام عملیات"
        },status = 403)     