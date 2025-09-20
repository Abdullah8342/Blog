'''
Permissions
'''

from rest_framework import permissions

class IsWriterOrReadOnly(permissions.BasePermission):
    '''
    Permissions for Writer to Edit,Delete,and Update Blog
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user



class CommentPermissions(permissions.BasePermission):
    '''
    Permissions for Writer to Edit,Delete,and Update Comment
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
