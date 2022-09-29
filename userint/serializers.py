from rest_framework import serializers
from .models import CustomUser,Roles



class CreateUserSerializer(serializers.Serializer):
    emai =serializers.EmailField()
    fullname =serializers.CharField()
    role=serializers.ChoiceField(Roles)


