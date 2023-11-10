from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email','first_name','last_name','password')
    search_fields=['email']
    list_filter=['email']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)