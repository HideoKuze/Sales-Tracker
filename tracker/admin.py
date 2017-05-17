from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import LoginInfo, Product, RevenueInfo, ExtendedProfile

class ProfileInline(admin.StackedInline):
	model = ExtendedProfile
	can_delete = False
	verbose_name_plural = "Amount Spent"

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(LoginInfo)
admin.site.register(Product)
admin.site.register(RevenueInfo)
