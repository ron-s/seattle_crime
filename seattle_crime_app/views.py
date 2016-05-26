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
    filter_fields = ('group', 'date', 'descriptio', 'block', 'latitude', 'longitude',)
    queryset = CrimeModel.objects.all()
    serializer_class = CrimeDataSerializer

    class Meta:
        model = CrimeModel
        abstract=True



def home_page(request):
    return render(request, 'index.html')





# ACCIDENT INVESTIGATION - traffic related
# ANIMAL COMPLAINTS
# ARREST - warrant calls
# ASSAULTS
# AUTO THEFTS - theft
# BIKE
# BURGLARY
# CAR PROWL
# DISTURBANCES
# DRIVE BY (NO INJURY) - gun calls
# FAILURE TO REGISTER (SEX OFFENDER) - sex offense no rape
# FALSE ALACAD - false alarms
# FALSE ALARMS
# FRAUD CALLS - forgery, identity theft, bad checks, 
# HARBOR CALLS - harbor emergencies
# HAZARDS
# LEWD CONDUCT - liquor violations
# LIQUOR VIOLATIONS
# MENTAL HEALTH
# MISCELLANEOUS MISDEMEANORS
# NARCOTICS COMPLAINTS
# NUISANCE, MISCHIEF
# OTHER PROPERTY - theft
# OTHER VICE - gambling, pron, 
# PERSON DOWN/INJURY - casualty non criminal-traffic, drug overdose, sick persons, injured, DOA
# PERSONS - LOST, FOUND, MISSING
# PROPERTY - MISSING, FOUND
# PROPERTY DAMAGE - property destruction, grang graffiti, 
# PROSTITUTION
# PROWLER
# RECKLESS BURNING
# ROBBERY
# SHOPLIFTING
# SUSPICIOUS CIRCUMSTANCES
# THREATS, HARASSMENT
# TRAFFIC RELATED CALLS
# TRESPASS
# VICE CALLS
# WEAPONS CALLS


