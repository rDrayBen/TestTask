from rest_framework import serializers
from .models import Restaurant, Menu, User


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'user']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'menu', 'date_created', 'votes_up', 'votes_down', 'restaurant']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role']
