import django_filters
from .models import Portfolio

class PortfolioFilter(django_filters.FilterSet):
    class Meta:
        model = Portfolio
        fields = {'speciality':['exact']}