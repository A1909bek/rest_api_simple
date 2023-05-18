from rest_framework import serializers
from .models import Pilot,Drone,DroneCategory,Competition

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='drone-detail')
    class Meta:
        model = DroneCategory
        fields = '__all__'

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    # drone_category = serializers.SlugRelatedField(queryset = DroneCategory.objects.all())
    class Meta:
        model = Drone
        fields = '__all__'

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()
    class Meta:
        model = Competition
        fields = '__all__'

class PilotSerializer(serializers.HyperlinkedModelSerializer): 
    competitions = CompetitionSerializer(many=True, read_only=True) 
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES) 
    gender_description = serializers.CharField( source='get_gender_display', read_only=True) 
    class Meta: 
        model = Pilot 
        fields = '__all__'


