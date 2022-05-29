# CRUD

from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['first_name', 'last_name', 'email']
        fields = ['first_name', 'last_name', 'birthday_year', 'email']