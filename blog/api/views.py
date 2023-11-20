from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import BloggerProfileSerializer

class CreateBlogger(GenericAPIView):
    serializer_class = BloggerProfileSerializer

    def post(self,request):
        print(request.user)        
        data = {
            "user":request.user.id,
            "description": request.data.get('description')
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "user": serializer.data,

        }) 
           
        