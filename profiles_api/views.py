from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

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
