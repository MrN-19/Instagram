from django.contrib import admin
from .models import *
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","register_date")
    list_filter = ("register_date",)
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ("user","ip","country","city")
    list_filter = ("country","city")
class FollowersFollowingAdmin(admin.ModelAdmin):
    list_display = ("following","followed")
    list_filter = ("following","followed")

class BlockUserAdmin(admin.ModelAdmin):
    list_display = ("user_is_blocking","user_is_blocked","action_date")
    list_filter = ("user_is_blocking","user_is_blocked")
class SearchHostoryAdmin(admin.ModelAdmin):
    list_display = ("user","search_date")
    list_filter = ("search_date","user")
class AccountSettingAdmin(admin.ModelAdmin):
    list_display = ("user","is_private_page","show_activity_status")
    list_filter = ("is_private_page","show_activity_status")   
class TwoFactorAuthenticationAdmin(admin.ModelAdmin):
    list_display = ("user","is_active","text_message")
    list_filter = ("is_active",)  
admin.site.register(Profile,ProfileAdmin)
admin.site.register(UserLocation,UserLocationAdmin)
admin.site.register(FollowersFollowing,FollowersFollowingAdmin)
admin.site.register(BlockUser,BlockUserAdmin)
admin.site.register(SearchHostory,SearchHostoryAdmin)
admin.site.register(AccountSetting,AccountSettingAdmin)
admin.site.register(TwoFactorAuthentication,TwoFactorAuthenticationAdmin)




