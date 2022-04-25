from django.urls import path
from .views import share_post_direct,direct,get_messages
app_name = "direct"
urlpatterns = [
    path("share",share_post_direct,name="sharepost"),
    path("direct",direct,name="direct"),
    path("get-messages",get_messages,name="getmessages"),
    
]