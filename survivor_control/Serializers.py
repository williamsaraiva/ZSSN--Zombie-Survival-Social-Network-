from django.db.models import Count
from rest_framework import serializers
from .models import survivor_control, survivor, infected, inventory


class survivor_controlSerializer(serializers.ModelSerializer):

    class Meta:
        model = survivor_control
        fields = ('id','status_title','status_message','last_location','survivor')

class survivorSerializer(serializers.ModelSerializer):
    infected_reports = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='status'
     )


    class Meta:
        model = survivor
        fields = ('id', 'survivor_name','gender','age','infected_reports')



class infectedSerializer(serializers.ModelSerializer):

    class Meta:
        model = infected
        fields = ('id','postby','survivor_infected')


class inventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = inventory
        fields = ('id','survivor','item_water','item_food','item_medication','item_ammunition')


