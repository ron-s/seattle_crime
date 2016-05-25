from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import CrimeModel

"""
Serializes geospatial fields from models into GeoJSON data.
"""

class CrimeDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CrimeModel
        geo_field = 'geom'
        fields = ('date', 'descriptio', 'group', 'subgroup', 'latitude', 'longitude',)
