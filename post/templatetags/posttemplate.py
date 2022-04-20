from django.template import Library

from post.models import PostLike,PostSave


register = Library()

def check_like_post(user,post):
    return PostLike.objects.filter(
        user = user,post = post
    ).exists()
def check_save_post(user,post):
    return PostSave.objects.filter(
        user = user,post = post
    ).exists()

register.filter("check_like",check_like_post)
register.filter("check_save",check_save_post)