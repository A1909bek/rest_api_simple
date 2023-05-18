from django.shortcuts import render 
from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from drones.models import DroneCategory 
from drones.models import Drone 
from drones.models import Pilot 
from drones.models import Competition 
from drones.serializers import DroneCategorySerializer 
from drones.serializers import DroneSerializer 
from drones.serializers import PilotSerializer 
from drones.serializers import CompetitionSerializer
from rest_framework import filters 
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter

class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    filter_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = ('name',)

class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'

class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_fields = ('name',)
    search_fields = ('name','drone_category')
    ordering_fields = ('name','inserted_timestamp')

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'

class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    filter_fields = ('name',)
    search_fields = ('name','races_count')
    ordering_fields = ('name','inserted_timestamp')

class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = 'competition-list'
    filter_fields = ('name',)
    search_fields = ('name','drone')
    ordering_fields = ('name','distance_achievement_date')

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'drone-categories': reverse(DroneCategoryList.name, request=request), 
            'drones': reverse(DroneList.name, request=request), 
            'pilots': reverse(PilotList.name, request=request), 
            'competitions': reverse(CompetitionList.name, request=request) })
    

