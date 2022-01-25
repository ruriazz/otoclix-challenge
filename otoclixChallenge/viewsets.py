from .models import Posts
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    def destroy(self, request, *args, **kwargs):
        old_data = self.get_object()
        serializer = PostSerializer(old_data)
        response = Response(serializer.data)
        self.perform_destroy(old_data)
        
        return response