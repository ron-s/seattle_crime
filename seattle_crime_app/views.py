from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import CrimeModel
from .serializers import (
    CrimeDataSerializer,
    )

"""
View Controller objects that render serialized GeoJSON data through the Django
REST GIS framework.
"""
class CrimeDataViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('date', 'descritio', 'blocklocat', 'latitude', 'longitude',)
    class Meta:
        abstract=True


class Crime2014DataViewSet(CrimeDataViewSet):
    queryset = CrimeModel.objects.all()
    serializer_class = CrimeDataSerializer


# class Crime2013DataViewSet(CrimeDataViewSet):
#     queryset = Crime2013.objects.all()
#     serializer_class = Crime2013DataSerializer


# class Crime2012DataViewSet(CrimeDataViewSet):
#     queryset = Crime2012.objects.all()
#     serializer_class = Crime2012DataSerializer


# class Crime2011DataViewSet(CrimeDataViewSet):
#     queryset = Crime2011.objects.all()
#     serializer_class = Crime2011DataSerializer


# class Crime2010DataViewSet(CrimeDataViewSet):
#     queryset = Crime2010.objects.all()
#     serializer_class = Crime2010DataSerializer

def home_page(request):
    return render(request, 'index.html')