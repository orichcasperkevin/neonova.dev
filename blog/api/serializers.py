from rest_framework import serializers
from blog.models import Blog,BloggerProfile,BlogTags

class BloggerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloggerProfile
        fields = ["user","description"]