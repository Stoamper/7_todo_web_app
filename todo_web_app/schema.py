from email.policy import default
import graphene
from graphene_django import DjangoObjectType
from todo_web_app.models import Project, TODO
from authnapp.models import User

# Test Query
# class TestQuery(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi, friend!")

# schema = graphene.Schema(query=TestQuery)

class TodoType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)

    def resolve_all_todos(root, info):
        return TODO.objects.all()

schema = graphene.Schema(query=Query)