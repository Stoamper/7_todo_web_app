# CRUD

from rest_framework.serializers import HyperlinkedModelSerializer
from unittest.util import _MAX_LENGTH
# from rest_framework import serializers

# from authnapp.serializers import UserModelSerializer
from .models import Project, TODO, TestProjectClass

#Ниже первичные сериализаторы (через Model)
class ProjectModelSerializer(HyperlinkedModelSerializer):
   class Meta:
        model = Project
        fields = '__all__'

class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'

# Рабочий
class TestProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TestProjectClass
        fields = '__all__'


# class TestProjectSerializer(ModelSerializer):
#     class Meta:
#         model = TestProjectClass
#         fields = '__all__'




#Сериализаторы для проверки (с ними надо разбираться)
#class ProjectSerializer(serializers.Serializer):
#    project_title = serializers.CharField(max_length = 200)
#    repo_link = serializers.URLField(max_length = 256)
#    users_in_project = UserModelSerializer(many=True)


#class TodoSerializer(serializers.ModelSerializer):
#    project = serializers.CharField(max_length = 200)
#    todo_text = serializers.CharField(max_length = 512)
#    created = serializers.DateTimeField()
#    modified = serializers.DateTimeField()
#    user = serializers.CharField(max_length = 200)


