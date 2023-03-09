from rest_framework import serializers
from .models import Pet, Type, Stat, Order, Category

class PetSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class TypeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class StatSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class OrderSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'