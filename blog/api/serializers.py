from rest_framework import serializers
from blog.models import BloggerProfile

class BloggerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloggerProfile
        fields = ["user","description"]

    def create(self,validated_data):    
        profile = BloggerProfile.objects.create(
            user = validated_data.get('user'),
            description = validated_data.get('description')
        )
        profile.save()
        return profile