from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer