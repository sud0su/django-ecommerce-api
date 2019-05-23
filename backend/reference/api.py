from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Carrier
from .serializers import CarriersSerializer

# Carrier via API
class CarrierAPIList(generics.ListAPIView):
    """ View to list all carriers """
    queryset = Carrier.objects.all().order_by('name')
    serializer_class = CarriersSerializer
    permission_classes = (IsAuthenticated, )
class CarrierAPICreate(generics.CreateAPIView):
    """ View to create a new carrier. Only accepts POST requests """
    queryset = Carrier.objects.all()
    serializer_class = CarriersSerializer
    permission_classes = (IsAuthenticated, )
class CarrierAPIRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a carrier or update carrier information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = Carrier.objects.all()
    serializer_class = CarriersSerializer
    permission_classes = (IsAuthenticated, )