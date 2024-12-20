from django.contrib import admin
from .models import GithubProfile

# Register your models here.
class GithubProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'followers', 'following')

admin.site.register(GithubProfile, GithubProfileAdmin)