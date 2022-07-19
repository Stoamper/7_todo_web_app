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

# Mutation
class UserMutation(graphene.Mutation):
    class Arguments:
        city = graphene.String(required=False)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, city, id):
        user = User.objects.get(pk=id)
        user.city = city
        user.save()
        return UserMutation(user=user)

class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()

class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    all_users = graphene.List(UserType)

    # Получить пользователя по имени
    user_by_firstName = graphene.Field(UserType, firstName=graphene.String(required=False))

    def resolve_all_todos(root, info):
        return TODO.objects.all()
    
    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_firstName(self, info, firstName):
        try:
            return User.objects.get(first_name=firstName)
        except User.DoesNotExist:
            return None

# schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query, mutation=Mutation)

# For GraphQL: allTodos + project + users
# {
#   allTodos
#   {id
#     project {
#     projectTitle
#     repoLink
#   }
#   todoText
#   created
#   modified
#   user {
#     firstName
#     lastName
#   }}
# }

# All users and projects by realted_name
# {
# 	allUsers {
#     firstName
#     lastName
#     todoSet {
#       project {
#         projectTitle
#       }
#     }
# 	}
# }

# Recursion
# {
#   allUsers {
#     firstName
#     lastName
#     todoSet {
#       project {
#         projectTitle
#         usersInProject {
#           firstName
#           lastName
#           isSuperuser
#         }
#       }
#     }
#   }
# }

# Find user and his projects
# {
#   userByFirstname(firstName: "Антон") {
#     firstName
#     lastName
#     projectSet {
#       projectTitle
#     }
#   }
# }

# For mutation user city
# mutation updateUser {
#   updateUser(city: "Perm", id: 1) {
#     user {
#       firstName
#       lastName
#       city
#     }
#   }
# }
