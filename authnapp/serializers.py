# CRUD

from rest_framework.serializers import HyperlinkedModelSerializer

from .models import User

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'birthday_year']
        # fields = ['first_name', 'last_name', 'birthday_year', 'email']

class UserModelSerializer_Test(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        # fields = ['first_name', 'last_name', 'birthday_year', 'email']

class UserModelSerializer_New(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_superuser', 'is_staff']
        # fields = ['first_name', 'last_name', 'birthday_year', 'email']