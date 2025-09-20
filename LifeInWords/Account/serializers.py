'''Account Serializers'''
from djoser.serializers import UserCreateSerializer as UCS


class UserCreateSerializer(UCS):
    '''
    Authentication Serializers
    '''
    class Meta(UCS.Meta):
        '''Meta'''
        fields = ['id','username','email','password','first_name','last_name']
