
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Project, TODO, TestProjectClass
from .serializers import ProjectModelSerializer, TodoModelSerializer, TestProjectSerializer
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .filters import ProjectFilter, TodoFilter

# Классы для пагинации
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


#Ниже простые ViewSet (ProjectModelSerializer и TodoModelSerializer). С ними работает
# class ProjectModelViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer
#     pagination_class = ProjectLimitOffsetPagination
#     filter_class = ProjectFilter

class ProjectModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filter_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filter_class = TodoFilter

    def close_todo(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Скорректированные представления для Project и Todo



# Ниже представлены тестовые класссы (в работе применять для отладки)
# Тестовый рабочий класс для представления
# При указанном renderer_class вывод осуществляется в JSON
# class TestProjectViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = TestProjectClass.objects.all()
#     serializer_class = TestProjectSerializer


# mixins_тестовый класс для проверки работы миксинов
# class TestProjectViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
#     queryset = TestProjectClass.objects.all()
#     serializer_class = TestProjectSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

#     @classmethod
#     def get_extra_actions(cls):
#         return []

# class TestProjectViewSet(ListAPIView):
#     # renderer_classes = [JSONRenderer]
#     queryset = TestProjectClass.objects.all()
#     serializer_class = TestProjectSerializer


# Тестовый вариант (позже удалить)
# class ProjectCreateAPIView(CreateAPIView):
#     renderer_classes = [JSONRenderer]
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer

#     @classmethod
#     def get_extra_actions(cls):
#         return []
