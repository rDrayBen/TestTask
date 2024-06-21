from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from models import Restaurant, Menu, User
from serializers import RestaurantSerializer, MenuSerializer, UserSerializer


class CreateRestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class UploadMenuView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CreateEmployeeView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentDayMenuView(APIView):
    def get(self, request):
        today = timezone.now().date()
        menus = Menu.objects.filter(date_created=today)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)


class CurrentDayResultsView(APIView):
    def get(self, request):
        today = timezone.now().date()
        menus = Menu.objects.filter(date_created=today)
        results = [
            {"menu": menu.menu, "votes_up": menu.votes_up, "votes_down": menu.votes_down}
            for menu in menus
        ]
        return Response(results)
