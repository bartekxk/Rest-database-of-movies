from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from rest_framework import viewsets,generics
from django.core import serializers
import django_filters.rest_framework
from rest_framework.response import Response
from restapi.serializers import MoviesSerializer, CommentsSerializer,TopSerializer
from .models import Movies,Comments
import json
from django.http import JsonResponse, HttpResponse
from rest_framework import status

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all().order_by('id')
    serializer_class = MoviesSerializer


class CommentsViewSet(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields=('Movie_ID',)
    def saveData(self,serializer):
        serializer.save()
    def post(self, request, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @classmethod
    def get_extra_actions(cls):
        return []

class TopViewSet(generics.ListAPIView):

   # queryset = Comments.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('date_from','date_to',)
    serializer_class = TopSerializer
    def sort(self, list):
        for i in range(0,len(list[0])-1):
            for j in range(0,len(list[0])-i-1):
                if list[1][j]<list[1][j+1]:
                    tmp=list[1][j]
                    list[1][j]=list[1][j+1]
                    list[1][j+1]=tmp
                    tmp=list[0][j]
                    list[0][j]=list[0][j+1]
                    list[0][j+1]=tmp
    def get(self, request, format=None):
        try:
            assert request.GET.get('date_from', False) != False and request.GET.get('date_to', False) != False
        except AssertionError:
            raise(AssertionError("Movies dates are required. Fore example /top?date_from=2000&date_to=2019"))
        try:
            date_from=int(request.GET['date_from'])
            date_to = int(request.GET['date_to'])
        except ValueError:
            raise ValueError("Date value error, it's must be year. For example: 2019")
        try:
            assert date_from>1000 and date_from<3000 and date_to>1000 and date_to<3000
        except AssertionError:
            raise ValueError("Date value error, it's must be year. For example: 2019")
        try:
            assert date_from <= date_to
        except AssertionError as e:
            raise(AssertionError('date_from can not be earlier than date_to'))
        comments_id = Comments.objects.values_list("Movie_ID", flat=True)
        movies_id = Movies.objects.values_list("id", flat=True)
        movies_year=Movies.objects.values_list("Year",flat=True)
        list = [[], [],[]]
        for item,year in zip(movies_id,movies_year):
            if len(year)!=4:
                year=year[:-1]
            print (year)
            if int(year)<=date_to and int(year)>=date_from:
                list[0].append(item)
                list[1].append(0)
        for item in comments_id:
            for i in range(0, len(list[0])):
                if list[0][i] == item:
                    list[1][i] = list[1][i] + 1
        self.sort(list)
        for i in range (0,len(list[0])):
            list[2].append(i+1)
        _json=[]
        for i in range(0,len(list[0])):
            record={'Movie_ID':list[0][i],'Rank':list[2][i],'Comments count':list[1][i]}
            _json.append(record)
        return JsonResponse(_json,safe=False)
    @classmethod
    def get_extra_actions(cls):
        return []