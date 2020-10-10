from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView (APIView):
    """ Test Class for Api View. """

    def get(self,request, format=None):
        """ Returns a List of Api View Feature """
        an_apiview =[
            'Uses HTTP method as a function(get,post,put,patch,delete)',
            'Similar to a traditional Django view',
            'Gives you the most control over your logic',
            'It mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})