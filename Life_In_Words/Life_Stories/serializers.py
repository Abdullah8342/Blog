from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import (
    MembershipPlan,
    UserMembership,
    Profile,
    Category,
    Series,
    Post,
    Tag,
    Comment
)



class ProfileSerializer(serializers.ModelSerializer):
    '''Profile'''
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        '''Meta'''
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'location',
            'about',
            'created_at',
            'updated_at',
            'user',
            # 'posts',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return Profile.objects.create(user = user,**validated_data)

class PostSerializer(serializers.ModelSerializer):
    ''' Post '''
    author = serializers.PrimaryKeyRelatedField(read_only = True)
    author_name = serializers.SerializerMethodField()

    def get_author_name(self,obj):
        '''Author Name'''
        profile = Profile.objects.get(user = self.context['request'].user)
        return profile.first_name

    class Meta:
        '''Meta'''
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'content',
            'cover_image',
            'created_at',
            'updated_at',
            'category',
            'is_published',
            'is_free',
            'order',
            'series',
            'author_name',
        ]

    def create(self, validated_data):
        author = self.context['author']
        return Post.objects.create(author = author,**validated_data)


class ReaderProfileSerializer(serializers.ModelSerializer):
    '''Only for Readers'''
    class Meta:
        '''Meta'''
        model = Profile
        fields = ['id','first_name','last_name']

class ReaderPostSerializer(serializers.ModelSerializer):
    ''' Post '''
    author = ReaderProfileSerializer()

    class Meta:
        '''Meta'''
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'content',
            'cover_image',
            'created_at',
            'updated_at',
            'category',
            'is_published',
            'is_free',
            'order',
            'series',
            'comment',
        ]



class CategorySerializer(serializers.ModelSerializer):
    '''Category'''
    post_count = serializers.IntegerField(read_only = True)
    class Meta:
        '''Meta'''
        model = Category
        fields = ['id','name','slug','post_count']


class CommentSerializer(serializers.ModelSerializer):
    '''Comment Serializer'''
    post = serializers.PrimaryKeyRelatedField(read_only = True)
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        '''Meta'''
        model = Comment
        fields = ['id','post','user','comment','rating']

    def create(self, validated_data):
        '''Create'''
        pk = self.context['pk']
        user = self.context['request'].user
        return Comment.objects.create(user = user,post_id = pk,**validated_data)
