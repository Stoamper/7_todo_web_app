from unicodedata import name
from django_filters import rest_framework as filters
from .models import Project, TODO

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='project_title', lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['project_title']

class TodoFilter(filters.FilterSet):
    # created = filters.DateTimeFilter(field_name='created')
    
    class Meta:
        model = TODO
        fields = ['todo_text']