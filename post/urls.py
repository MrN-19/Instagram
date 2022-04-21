from django.urls import path
from .views import like_post,save_post,get_users_to_share_post,get_picture_by_username,get_user_by_id, set_comment,get_comments_by_post_id
app_name = "post"
urlpatterns = [
    path("like-post",like_post,name="like-post"),
    path("save-post",save_post,name="save-post"),
    path("share-post-user",get_users_to_share_post,name="sharepostuser"),
    path("usernamepicture/<str:username>/",get_picture_by_username,name="getpicturebyusername"),
    path("set-comment/<str:text>/<str:postid>/<int:header>",set_comment,name="setcomment"),
    path("comments/<str:postid>",get_comments_by_post_id,name="getcommentsbypostid"),
    path("user/<int:id>",get_user_by_id,name="getuserbyid"),

]