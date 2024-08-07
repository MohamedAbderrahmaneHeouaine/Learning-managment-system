from django.contrib import admin
from userauths.models import *


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name']


admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)
