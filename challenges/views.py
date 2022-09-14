from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import include, path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from challenges import serializer
from django.contrib.auth.models import User

# Create your views here.


class Helloapiview (APIView):
    """Test Api View"""
    serializer_class=serializer.HelloSerializer

    def get(self, request, format=None):
        """returns a list of api views feature"""
        an_apiview = [
            'uses http methods as function (get,post ,patch ,put ,delete)',
            'is similar to a traditional django view',
            'gives u the most control ur app logic',
            'is mapped manually to urls ',
        ]
        return Response({'message': 'hello ', 'apiview': an_apiview})
    
    def post(self,request):
        """create a hello msg with our name """
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello  {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)    

    def put(self,request,pk=None): #bnshil al bta3 kolo w n8iro
        """Handling update an object """
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handle a partial update of an object"""   #update goz2 mn al input so8ir w nzod feh 
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """delete object on data base """
        return Response({'method':'DELETE'})

