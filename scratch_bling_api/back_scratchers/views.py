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


class GetBackScratchersView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, search_term=None):
        if search_term:
            back_scratchers = BackScratchers.objects.filter(
                Q(name__icontains=search_term) | Q(description__icontains=search_term))
        else:
            back_scratchers = BackScratchers.objects.filter().all()
        if back_scratchers or len(back_scratchers) > 0:
            serializer_context = {
                'request': request,
            }
            serialized = BackScratchersSerializer(back_scratchers, context=serializer_context, many=True)
            return Response(serialized.data)
        else:
            return Response(
                {'No Back Scratchers': 'Sorry no back scratchers were found with search term ' + search_term})


class CreateBackScratchersView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if request.method != 'POST':
            return Response({'error': 'Invalid request type'})
        else:
            data = request.data
            new_back_scratcher = BackScratchers(name=data['name'], description=data['description'])
            size_list = []
            for size in data['size']:
                try:
                    current_size = Size.objects.filter(size__iexact=size)
                except Exception as e:
                    return Response({'error': size + ' does not exist'}, status=400)
                if current_size:
                    size_list.append(current_size[0])
                else:
                    print('for some reason didnt find the size ')
                    size = Size(data['size'])
                    size.save()
                    size_list.append(size)
            new_back_scratcher.save()
            new_back_scratcher.size.set(size_list)

            return Response({'success': f'Back Scratcher {new_back_scratcher.name} added',
                             'id': new_back_scratcher.id})


class UpdateBackScratcherView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        data = request.data
        if 'id' not in data.keys():
            return Response({'error': 'id required for update'}, status=400)
        else:
            try:
                back_scratcher = BackScratchers.objects.get(id=data['id'])
            except Exception as e:
                return Response({'error': str(data['id']) + ' does not exist'}, status=400)
            if 'name' in data.keys():
                back_scratcher.name = data['name']
            if 'description' in data.keys():
                back_scratcher.description = data['description']
            if 'size' in data.keys():
                size_list = []
                for size in data['size']:
                    try:
                        current_size = Size.objects.filter(size__iexact=size)
                    except Exception as e:
                        return Response({'error': size + ' does not exist'}, status=400)
                    if current_size:
                        size_list.append(current_size[0])
                back_scratcher.size.set(size_list)
            back_scratcher.save()
            return Response({'success': f'Back Scratcher {back_scratcher.name} updated'})


class DeleteBackScratcherView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        deleted_scratchers = []
        not_deleted_scratchers = []
        if 'id' not in data.keys():
            return Response({'error': 'ID required for deletion'}, status=400)
        else:
            if type(data['id']) == int or type(data['id']) == str:
                try:
                    back_scratcher = BackScratchers.objects.get(id=int(data['id']))
                    back_scratcher.delete()
                    deleted_scratchers.append(int(data['id']))
                except Exception as e:
                    not_deleted_scratchers.append((data['id']))
            elif type(data['id']) == list:
                for scratcher_id in data['id']:
                    try:
                        back_scratcher = BackScratchers.objects.get(id=(int(scratcher_id)))
                        back_scratcher.delete()
                        deleted_scratchers.append(scratcher_id)
                    except Exception as e:
                        not_deleted_scratchers.append(int(scratcher_id))
            return Response({'successful_deletions': deleted_scratchers, 'failed_deletions': not_deleted_scratchers})
