# from django.shortcuts import render
import json

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from .models import BackScratchers
from .serializers import BackScratchersSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@api_view(['GET'])
def get_back_scratchers(request, search_term):
    back_scratchers = BackScratchers.objects.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term))
    if back_scratchers or len(back_scratchers) > 0:
        serializer_context = {
            'request': request,
        }
        serialized = BackScratchersSerializer(back_scratchers, context=serializer_context, many=True)
        return Response(serialized.data)
    else:
        return Response({'No Back Scratchers': 'Sorry no back scratchers were found with search term '+search_term})


