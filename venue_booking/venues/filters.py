import django_filters
from .models import Venue

class VenueFilter(django_filters.FilterSet):
    price_per_hour = django_filters.RangeFilter()
    capacity = django_filters.RangeFilter()
    amenities = django_filters.ModelMultipleChoiceFilter(queryset=Amenity.objects.all())

    class Meta:
        model = Venue
        fields = ['category', 'price_per_hour', 'capacity', 'amenities']