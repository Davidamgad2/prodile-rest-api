from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import include, path
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from challenges import serializer, models, permissions


# Create your views here.


class Helloapiview (APIView):
    """Test Api View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """returns a list of api views feature"""
        an_apiview = [
            'uses http methods as function (get,post ,patch ,put ,delete)',
            'is similar to a traditional django view',
            'gives u the most control ur app logic',
            'is mapped manually to urls ',
        ]
        return Response({'message': 'hello ', 'apiview': an_apiview})

    def post(self, request):
        """create a hello msg with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello  {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):  # bnshil al bta3 kolo w n8iro
        """Handling update an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""  # update goz2 mn al input so8ir w nzod feh
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete object on data base """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset """

    serializer_class = serializer.HelloSerializer

    def list(request, self):
        """return hello message"""
        a_viewset = [
            'uses actions (list,create,retreive,update,partial_update',
            'automatically maps urls using router ',
            'provides more functionality using less code',
        ]
        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, requset):
        """create a new hello message"""
        serializer = self.serializer_class(data=requset.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its id """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle and updating object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handling partial update for the object"""
        return Response({'http_method': 'Patch'})

    def destroy(self, request, pk=None):
        """handling destroy the object"""
        return Response({'http_method': 'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles """
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # how the user will auth the mechanism and permission says how the user gets permission to do the certain things
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateownprofile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class userloginapiview(ObtainAuthToken):
    """handling  creating user auth token """
    
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES