from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializers


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
