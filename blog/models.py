from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class MarkdownxField(models.TextField):
    """
        Custom Django field for Markdown text        
    """
    pass

class BloggerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = MarkdownxField(max_length=500,unique=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            BloggerProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        if hasattr(instance,'bloggerprofile'):
            instance.hankoprofile.save()

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Blog(models.Model):
    blogger = models.ForeignKey(BloggerProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = MarkdownxField()

class BlogTags(models.Model):
    blog =  models.ForeignKey(Blog,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)