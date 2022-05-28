# CRUD

from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, TODO

class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'email']
        # fields = ['first_name', 'last_name', 'birthday_year']

class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'