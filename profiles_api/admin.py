from django.contrib import admin
from profiles_api import models

# Register your models here.
admin.site.register(models.UserProfile) #registers UserProfile model, makes it accessible through admin interface
admin.site.register(models.ProfileFeedItem)