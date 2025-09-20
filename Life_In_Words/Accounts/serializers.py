from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    '''USER CREATE SERIALIZERS'''
    class Meta(BaseUserCreateSerializer.Meta):
        '''CUSTOM SERAILIZERS'''
        fields = ['id','username','first_name','last_name','password','email']
