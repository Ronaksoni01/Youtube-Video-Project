from django.contrib import admin
from .models import Youtube
# Register your models here.

# class YoutubeAdmin(admin.ModelAdmin):
#     list_display =('title','video_id','url')


admin.site.register(Youtube)