from django.http import JsonResponse
from django.shortcuts import render,redirect
from pkg_resources import require
from account.models import *
from post.models import *
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from direct.models import DirectMessage

def get_new_messages(user):
    new_messages = DirectMessage.objects.filter(
        reciver = user,seen_state = False,send_state = True
    )
    return new_messages


def home(request):
    profile = Profile.objects.get(user = request.user)
    current_user_followers = FollowersFollowing.objects.filter(followed = request.user)
    current_user_followings = FollowersFollowing.objects.filter(following = request.user)
    posts = []
    print(current_user_followings)
    for i in current_user_followings:
        posts.append(
            i.followed.userposts.order_by("-publish_date").first()
        )

    context = {
        "profile" : profile,
        "posts" : posts,
        "followings" : current_user_followings,
        "followers" : current_user_followers,
        "new_messages" : get_new_messages(request.user)
    }
    return render(request,"home.html",context)

@require_GET
@login_required(login_url="account:login")
def new_messages(request):
    try:
        messages = get_new_messages(request.user)
        messages = serialize(messages)
        data = {
            "status" : True,"message" : "Success 200","data" : messages
        }
        return JsonResponse(data,status = 200)
    except:
        return JsonResponse({
            "status" : False,
            "message" : "Bad Request 403",
            "text" : "خطایی رخ داده است"
        },status = 403)
