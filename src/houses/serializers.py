from rest_framework import serializers
from .models import House
from rest_framework.renderers import JSONRenderer



class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        #fields = ['name', 'price', 'description', 'photo', 'active']
        fields = '__all__'