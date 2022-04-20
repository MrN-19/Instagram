from django.urls import path
from .views import share_post_direct
app_name = "direct"
urlpatterns = [
    path("share",share_post_direct,name="sharepost"),
]