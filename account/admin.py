from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    Profile admin model
    """
    list_display =  ["user",]
    search_fields = ["user__username", "user__email"]


admin.site.register(Profile, ProfileAdmin)
