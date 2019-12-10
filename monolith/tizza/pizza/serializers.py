from rest_framework import serializers

from .models import Pizza, Pizzeria, Likes


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Pizza
        fields = ('id', 'title', 'description')


class PizzeriaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Pizzeria
        fields = ('address', 'phone')
