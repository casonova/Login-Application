from django.contrib import admin
from profileapp.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'profile_img')
    search_fields = ['phone_number']
    list_filter = ['phone_number']


admin.site.register(Profile, ProfileAdmin)

