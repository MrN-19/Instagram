from django.contrib import admin
from .models import *

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ("user","post","liked_date")



admin.site.register(LocationTag)

admin.site.register(HashTag)

admin.site.register(AllowedExtensions)

admin.site.register(Post)

admin.site.register(PostLike,PostLikeAdmin)
admin.site.register(PostComment)
admin.site.register(CommentLike)
admin.site.register(PostSave)
