import django_filters
from .models import Student


class MyFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    
    def filter_search(self, queryset, name, value):
        return queryset.filter(
            surname__iexact=value
        ) | queryset.filter(
            name__iexact=value
        )

    class Meta:
        model = Student
        fields = ('surname', 'name', 'grade')
