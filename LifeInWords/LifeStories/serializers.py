'''Serialisers for blog models'''
from rest_framework import serializers
from .models import Profile,Post,Comment,Categories


class ProfileSerializers(serializers.ModelSerializer):
    '''
    Profile Serializser
    '''
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        '''
        Serialisers Meta Class
        '''
        model = Profile
        fields = ['id','user','image','bio','phone_no','facebook','instagram','linkedin']


    def create(self, validated_data):
        user = self.context['request'].user
        return Profile.objects.create(user = user,**validated_data)


class PostSerializers(serializers.ModelSerializer):
    '''
    BlogPost Serialiser
    '''
    author = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        '''
        Serialisers Meta Class
        '''
        model = Post
        fields = ['id','title','author','slug','content','image','categories','dateTime']


    def create(self, validated_data):
        user = self.context['request'].user
        print(user)
        return Post.objects.create(author = user,**validated_data)


class CommentSerializers(serializers.ModelSerializer):
    '''
    Comment Serialisers
    '''
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    blog = serializers.PrimaryKeyRelatedField(read_only = True)
    dateTime = serializers.DateTimeField(read_only = True)
    class Meta:
        '''
        Comment Meta
        '''
        model = Comment
        fields = ['id','user','content','blog','dateTime']


    def create(self, validated_data):
        user = self.context['request'].user
        post_id = self.context['blog']
        post = Post.objects.get(id = post_id)
        return Comment.objects.create(user = user, blog = post,**validated_data)


class CategoriesSerializers(serializers.ModelSerializer):
    '''Categories Serializers'''
    class Meta:
        '''Meta'''
        model = Categories
        fields = ['id','post','title']
