from curses.ascii import US
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User
from .serializers import UserModelSerializer, UserModelSerializer_Test, UserModelSerializer_New
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination

# Класс для пагинации
class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5

# Первоначальное представление для User
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializer_Test
        return UserModelSerializer

# Скорректированное представление для User (просмотр списка и каждого пользователя, изменения, нельзя удалять и создавать)
class UserCustomViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializer_Test
        if self.request.version == '0.3':
            return UserModelSerializer_New    
        return UserModelSerializer