from django.contrib import admin
from .models import DirectMessage

class DirectMessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(DirectMessage)
