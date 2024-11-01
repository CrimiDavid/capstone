from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking  # Replace with the actual model name and path if different
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Class to handle POST and GET requests for Menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()  # Retrieves all menu items
    serializer_class = MenuItemSerializer  # Uses MenuSerializer for data handling

# Class to handle GET, PUT, and DELETE requests for single Menu items
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Retrieves specific menu item by ID
    serializer_class = MenuItemSerializer  # Uses MenuSerializer for data handling

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    """
    A viewset for viewing and editing booking instances.
    """
    queryset = Booking.objects.all()  # Fetches all Booking model objects
    serializer_class = BookingSerializer  # Specifies the serializer for data handling
