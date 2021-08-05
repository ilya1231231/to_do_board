from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView
from rest_framework import generics, permissions
# from .serializers import ProfileSer
from django.shortcuts import HttpResponse
from .models import Profile
from django.contrib.auth.models import User


# class ProfileCreateView(generics.CreateAPIView):
# serializer_class = ProfileSer


# def profile(request):
# return render(request, 'profile/user-profile.html')


def test(request):     # username):
    #users = User.objects.filter(username=pk)
    #u = User.objects.get(username=username)
    #show = Profile.objects.all()
    #url = reverse('profile/user-profile.html', kwargs={'username': u})

    #print(Profile.objects.filter(user=users[0].id)[0])

    return render(request, 'profile/user-profile.html') #username)
