from django.contrib import admin
from .models import Blog,Tag,BlogTags,BloggerProfile
# Register your models here.
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(BlogTags)
admin.site.register(BloggerProfile)