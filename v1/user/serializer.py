<<<<<<< HEAD
from typing import Any, Dict
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from v1.user.models import  User


class MyTokenSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        res = super().validate(attrs)
        res['user'] = {
            "id" : self.user.id,
            "first_name" : self.user.first_name,
            "last_name" : self.user.last_name,
            "phone" : self.user.phone
        }
        
        return res
    
    
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "password")
        

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "phone")
    
    
    
    
=======
from typing import Any, Dict
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from v1.user.models import  User


class MyTokenSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        res = super().validate(attrs)
        res['user'] = {
            "id" : self.user.id,
            "first_name" : self.user.first_name,
            "last_name" : self.user.last_name,
            "phone" : self.user.phone
        }
        
        return res
    
    
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "password")
        

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "phone")
    
    
    
    
>>>>>>> d51e158 (..)
    