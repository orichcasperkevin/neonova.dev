from django.urls import  path
from .views import CreateBlogger
urlpatterns = [
    path("create-blogger/", CreateBlogger.as_view()),
]   
    