from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.urls import include,path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
# Create your views here.
class Helloapiview (APIView):
    """Test Api View"""
    def get(self,request,format=None):
        """returns a list of api views feature"""
        an_apiview=[
            'uses http methods as function (get,post ,patch ,put ,delete)',
            'is similar to a traditional django view',
            'gives u the most control ur app logic',
            'is mapped manually to urls ',
        ]
        return Response({'message':'hello','apiview':an_apiview})