
from rest_framework import serializers
from django.contrib.auth.models import User
from studApp.models import StudentModel

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password','email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'
        read_only_fields=['id','owner']
