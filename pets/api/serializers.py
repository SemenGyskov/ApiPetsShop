from rest_framework import serializers
from .models import Pet, Type, Stat, Order, Category

class PetSerialiser(serializers.Serializer):
    class Meta:
        model = Pet
        fields = '__all__'

class TypeSerialiser(serializers.Serializer):
    class Meta:
        model = Type
        fields = '__all__'

class StatSerialiser(serializers.Serializer):
    class Meta:
        model = Stat
        fields = '__all__'

class OrderSerialiser(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'

class CategorySerialiser(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'