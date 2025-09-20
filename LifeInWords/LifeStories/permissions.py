'''Custom permission classes'''
from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsSuperUserIsOwnerOrReadOnly(BasePermission):
    '''
    Custom Permission Class Only Super and the Owner can Manuplate the object
    '''
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user == obj.author:
            return True
        return False
