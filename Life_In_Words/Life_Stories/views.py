from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (
    PostSerializer,
    ProfileSerializer,
    CategorySerializer,
    ReaderPostSerializer,
    CommentSerializer,
)
from .models import Post,Profile,Category,Comment


class ProfileApiView(APIView):
    '''Profile API Views'''

    def get(self,request):
        '''GET'''
        user_profile = get_object_or_404(Profile,user = request.user)
        serializer = ProfileSerializer(user_profile,context = {'request':request})
        return Response(serializer.data)

    def post(self,request):
        '''POST'''
        serializer = ProfileSerializer(data = request.data ,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        '''PATCH'''
        user_profile = get_object_or_404(Profile,user = request.user)
        serializer = ProfileSerializer(instance = user_profile,data = request.data,partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request):
        '''DELETE'''
        user_profile = get_object_or_404(Profile,user = request.user)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostsApiView(APIView):
    '''PostsApiView'''

    def get(self,request):
        '''GET'''
        profile = get_object_or_404(Profile,user = request.user)
        queryset = Post.objects.filter(author = profile)
        serializer = PostSerializer(queryset,many = True,context={'request':request})
        return Response(serializer.data)

    def post(self,request):
        '''POST'''
        profile = get_object_or_404(Profile,user = request.user)
        serializer = PostSerializer(
            data = request.data,
            context = {'request':request,'author':profile}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostApiView(APIView):
    '''Post'''
    def get(self,request,pk):
        '''GET'''
        profile = get_object_or_404(Profile,user = request.user)
        queryset = Post.objects.filter(author = profile,pk = pk)
        serializer = PostSerializer(queryset,many = True,context={'request':request})
        return Response(serializer.data)

    def patch(self,request,pk):
        '''PATCH'''
        profile = get_object_or_404(Profile,user = request.user)
        queryset = get_object_or_404(Post,author = profile,pk = pk)
        serializer = PostSerializer(
            instance = queryset,data = request.data,
            partial = True,context={'request':request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        '''Delete'''
        profile = get_object_or_404(Profile,user = request.user)
        queryset = get_object_or_404(Post,author = profile,pk = pk)
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



class ReaderPostsAPIView(APIView):
    '''Reader Posts Api View'''
    def get(self,request):
        '''GET'''
        queryset = Post.objects.select_related('author').prefetch_related('comment').filter(is_published = True)
        serializer = ReaderPostSerializer(queryset,many = True,context = {'request':request})
        return Response(serializer.data)

class ReaderPostDetailAPIView(APIView):
    '''Reader Posts Api View'''
    def get(self,request,pk):
        '''GET'''
        queryset = Post.objects.select_related('author').prefetch_related('comment').filter(is_published = True,pk = pk)
        serializer = ReaderPostSerializer(queryset,many = True,context = {'request':request})
        return Response(serializer.data)




class CategoryApiView(APIView):
    '''Category'''
    def get(self,request):
        '''GET'''
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset,many = True)
        return Response(serializer.data)


class CommentApiView(APIView):
    '''Comment APIView'''
    def get(self,request,pk):
        '''Post'''
        queryset = Comment.objects.filter(post = pk)
        serializer = CommentSerializer(queryset,many = True)
        return Response(serializer.data)

    def post(self,request,pk):
        '''Post'''
        serializer = CommentSerializer(data = request.data,context={'request':request,'pk':pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Success Message':'Comment added successfuly'})


