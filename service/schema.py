import graphene
from graphene_django import DjangoObjectType

from library.models import Author, Book
from to_do.models import ToDo, Project


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = "__all__"


class AuthorMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        uuid = graphene.UUID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, birthday_year, uuid):
        author = Author.objects.get(uuid=uuid)
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation(author=author)


class TodoMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        uuid = graphene.UUID()

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, text, uuid):
        todo = ToDo.objects.get(uuid=uuid)
        todo.text = text
        todo.save()
        return TodoMutation(todo=todo)


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()
    update_todo = TodoMutation.Field()




class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class Query(graphene.ObjectType):

    all_todo = graphene.List(TodoType)
    all_projects = graphene.List(ProjectType)
    all_authors = graphene.List(AuthorType)
    all_books = graphene.List(BookType)
    author_by_uuid = graphene.Field(AuthorType, uuid=graphene.UUID(required=True))
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=False))

    todos_by_project = graphene.List(TodoType, project=graphene.String(required=False))
    todo_by_uuid = graphene.Field(TodoType, uuid=graphene.UUID(required=True))

    def resolve_all_todo(self, info):
        return ToDo.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_authors(self, info):
        return Author.objects.all()

    def resolve_all_books(self, info):
        return Book.objects.all()

    def resolve_author_by_uuid(self, info, uuid):
        try:
            return Author.objects.get(uuid=uuid)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(self, info, name=None):
        books = Book.objects.all()
        if name:
            return books.filter(author__first_name=name)
        return books

    def resolve_todos_by_project(self, info, project=None):
        todos = ToDo.objects.all()
        if project:
            return todos.filter(project__title=project)
        return todos

    def resolve_todo_by_uuid(self, info, uuid):
        try:
            return ToDo.objects.get(uuid=uuid)
        except ToDo.DoesNotExist:
            return None



schema = graphene.Schema(query=Query, mutation=Mutation)



