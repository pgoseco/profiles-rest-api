from rest_framework.views import APIView, Response





class HelloApiView(APIView):
    """Test API View"""

    def GetRequest(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP Methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
            'Hi, My name is Patrick',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

