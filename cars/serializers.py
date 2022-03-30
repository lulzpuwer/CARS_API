from rest_framework import serializers
from .models import Car


class Car_serializer(serializers.ModelSerializer):
  class meta:
    model = Car
    fields = ['id','make', 'model', 'yr', 'price']