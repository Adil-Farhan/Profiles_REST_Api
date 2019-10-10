from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions

    """Test Api View"""
    serializer_class = serializers.HelloSerializers
    class HelloApiView(APIView):


    def get(self,request,format=None):
        """Returns a list of API Views"""
        an_apiview = [
        'Uses http method as a function (get, post, patch, delete,put)',
        'Is smilar to traditional  Djaongo View',
        'Give you the most control over application logic',
        'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello !','an_apiview': an_apiview} )
        """ Dictionary is passed to this Response """

    def post(self,request):
        """cerate a message with name """
        serializer =   self.serializer_class(data = request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            # message=f'Hello {name}'
            message = 'Hello ' + name


            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Update the complete object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Update the partial object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk = None ):
        """Delete the object """
        return Response({'method':'DELETE'})

class HelloViewSets(viewsets.ViewSet):
    """Test Api View Set"""

    serializer_class = serializers  .HelloSerializers

    def list(self,request):
        """Returnds a list"""
        a_viewList = [
        'Uses http method as a function (get, post, patch, delete,put)',
        'Is smilar to traditional  Djaongo View',
        'Give you the most control over application logic',
        'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello','a_viewList':a_viewList})


    def create(self,request):
        """Create a new hello message"""
        serializer =  self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Helloo ' + name + ' !'
            return Response({'message':message })
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """ Handle getting object by Id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ Handle UPDATING object by Id"""
        return Response({'http_method':'UPDATE'})

    def partial_update(self,request,pk=None):
        """ Handle partial update object by Id"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """ Handle destroy update object by Id"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle and Create/Updating profiles"""
    serializer_class =  serializers.UserProfileSerailizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
