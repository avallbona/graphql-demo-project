import pytest
from graphene.test import Client
from model_bakery import baker, seq

from api.schema import schema


@pytest.fixture
def graphql_client():
    return Client(schema)


@pytest.fixture
def books():
    yield baker.make("api.Book", title=seq("title "), _quantity=3)


@pytest.fixture
def single_book():
    yield baker.make("api.Book", id=1, title="single book title")
