from django.contrib import admin
from .models import AppInfo

class AppInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(AppInfo,AppInfoAdmin)