from rest_framework import serializers
from .models import UsersData


#Rest Framework Serializer
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersData
        fields = ('id','first_name','last_name','company_name','age','city','state','zip','email','web')