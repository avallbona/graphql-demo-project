import pytest
from graphene.test import Client
from model_bakery import baker

from api.models import Book
from api.schema import schema


@pytest.fixture
def graphql_client():
    return Client(schema)


@pytest.fixture
def books():
    books = [
        baker.make(
            Book,
            title="django for professionals",
            year_published="2020",
            review=5,
        ),
        baker.make(Book, title="react for beginners", year_published="2020", review=3),
        baker.make(
            Book, title="javascript for dummies", year_published="2020", review=1
        ),
        baker.make(Book, title="css for dummies", year_published="2021", review=4),
        baker.make(Book, title="html for dummies", year_published="2021", review=2),
    ]

    yield books


@pytest.fixture
def single_book():
    yield baker.make("api.Book", id=1, title="single book title")
