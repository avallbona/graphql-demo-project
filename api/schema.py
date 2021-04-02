import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"
        filter_fields = {
            "id": ["exact"],
            "title": ["exact", "icontains", "istartswith"],
            "author": ["exact", "icontains", "istartswith"],
            "year_published": ["exact"],
            "review": ["exact"],
        }
        interfaces = (Node,)


class Query(graphene.ObjectType):
    book = Node.Field(BookType)
    all_books = DjangoFilterConnectionField(BookType)

    # all_books = graphene.List(BookType)
    # book = graphene.Field(BookType, book_id=graphene.Int())
    # book_by_year = graphene.List(BookType, year=graphene.String())
    # book_by_author = graphene.List(BookType, author=graphene.String())

    # def resolve_all_books(self, info, **kwargs):
    #     return Book.objects.all()
    #
    # def resolve_book(self, info, book_id):
    #     return Book.objects.get(pk=book_id)
    #
    # def resolve_book_by_year(self, info, year):
    #     return Book.objects.filter(year_published=year)
    #
    # def resolve_book_by_author(self, info, author):
    #     return Book.objects.filter(author__icontains=author)


class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int()


class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book(
            title=book_data.title,
            author=book_data.author,
            year_published=book_data.year_published,
            review=book_data.review,
        )
        book_instance.save()
        return CreateBook(book=book_instance)


class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):

        book_instance = Book.objects.get(pk=book_data.id)

        if book_instance:
            book_instance.title = book_data.title
            book_instance.author = book_data.author
            book_instance.year_published = book_data.year_published
            book_instance.review = book_data.review
            book_instance.save()

            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        book_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
