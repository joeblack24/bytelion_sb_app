# from django.shortcuts import render
import json

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import BackScratchers, Size
from .serializers import BackScratchersSerializer, SizeSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@api_view(['GET'])
def get_back_scratchers(request, search_term = None):
    if search_term:
        back_scratchers = BackScratchers.objects.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term))
    else:
        back_scratchers = BackScratchers.objects.filter().all()
    if back_scratchers or len(back_scratchers) > 0:
        serializer_context = {
            'request': request,
        }
        serialized = BackScratchersSerializer(back_scratchers, context=serializer_context, many=True)
        return Response(serialized.data)
    else:
        return Response({'No Back Scratchers': 'Sorry no back scratchers were found with search term '+search_term})


@api_view(['POST'])
def create_back_scratcher(request):
    if request.method != 'POST':
        return Response({'error': 'Invalid request type'})
    else:
        # try:
        print(f'type {type(request.data)}')
        print(f'Request data:{request.data}')
        data = request.data
        print(f'parsed data - {data}')
        print('size type: ', type(data['size']))
        new_back_scratcher = BackScratchers(name=data['name'], description=data['description'])
        size_list=[]
        for size in data['size']:
            current_size = Size.objects.filter(size__iexact=size)
            print(f'got size {current_size}')
            if current_size:
                size_list.append(current_size[0])
            else:
                print('for some reason didnt find the size ')
                size = Size(data['size'])
                size.save()
                size_list.append(size)
        new_back_scratcher.save()
        new_back_scratcher.size.set(size_list)
        print('size set')
        print('new_back_scratcher:',new_back_scratcher)

        return Response({'success': f'Back Scratcher {new_back_scratcher.name} added',
                         'id': new_back_scratcher.id})

@api_view(['PUT'])
def update_back_scratcher(request):
    if request.method != 'PUT' or request.method != 'POST':
        return Response({'error': 'Invalid request type'})
