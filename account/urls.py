from django.urls import path
from . import views
app_name = "account"

urlpatterns = [
    path("request-action",views.follow_unfollow_user,name="followunfollow"),
    path("block-user-post",views.block_user_by_post,name="blockuserbypost"),
    
]