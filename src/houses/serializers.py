from rest_framework import serializers
from .models import House
from rest_framework.renderers import JSONRenderer



class HouseSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField()
    photo = serializers.ImageField()
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return House.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance