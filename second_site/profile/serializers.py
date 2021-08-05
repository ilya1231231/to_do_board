from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


#class UserSer(serializers.ModelSerializer):
    #"""Сериализация пользователя"""
    #class Meta:
        #model = User
        #fields = ('username', 'email')

#class ProfileSer(serializers.ModelSerializer):

   # class Meta:
       # model = Profile
       # fields = '__all__'
