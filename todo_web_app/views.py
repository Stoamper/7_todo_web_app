from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class TodoModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TodoModelSerializer


#Ниже заглушки, когда был ProjectModelSerializer и TodoModelSerializer
#class ProjectModelViewSet(ModelViewSet):
#    queryset = Project.objects.all()
#    serializer_class = ProjectModelSerializer

#class TodoModelViewSet(ModelViewSet):
#    queryset = TODO.objects.all()
#    serializer_class = TodoModelSerializer

#class UserModelViewSet(ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserModelSerializer






#class UserModelViewSet(ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserModelSerializer