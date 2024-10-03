from django.contrib import admin

# Register your models here.
from bugapp.models import UserProfile, Comment, Bug, Project

admin.site.register(UserProfile)
admin.site.register(Bug)
admin.site.register(Project)
admin.site.register(Comment)
