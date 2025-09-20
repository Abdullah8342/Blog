"""Module providing a function for blog website"""


from django.shortcuts import get_object_or_404


from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status


from .serializers import ProfileSerializers,PostSerializers,CommentSerializers
from .permissions import IsSuperUserIsOwnerOrReadOnly
from .models import Post,Comment,Profile


class BlogsViewset(ModelViewSet):
    '''
    API VIEW
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    def get_serializer_context(self):
        return {"request":self.request}
    permission_classes = [IsAuthenticatedOrReadOnly,IsSuperUserIsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    filterset_fields = []
    search_fields = ['title','slug','categories']


class CommentViewset(ModelViewSet):
    '''
    Add comment
    '''
    def get_queryset(self):
        return Comment.objects.filter(blog = self.kwargs['blog_pk'])
    serializer_class = CommentSerializers
    def get_serializer_context(self):
        return {'request':self.request,'blog':self.kwargs['blog_pk']}
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileApiView(APIView):
    '''
    Profile
    '''

    def get(self):
        '''
        profile
        '''
        profile = get_object_or_404(Profile,user = self.request.user)
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)


    def post(self):
        '''
        Create Profile
        '''
        data = self.request.data
        serializer = ProfileSerializers(data = data,context = {'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status':'created successfuly'})


class EditProfile(APIView):
    '''
    Edit Profile
    '''
    def patch(self,request):
        '''
        Update Method
        '''
        try:
            # Retrieve the item by Id
            profile = get_object_or_404(Profile,user = self.request.user)
        except profile.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        # Partially update with incoming data serializer
        # Itemserializer(item, data-request.data, partial-True)
        serializer = ProfileSerializers(profile,data = request.data,partial = True,)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    permission_classes = [IsAuthenticated]
