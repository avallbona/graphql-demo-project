import pytest


@pytest.fixture
def query_all_books():
    return """
    query {
      allBooks {
        id
        title
        author
        yearPublished
        review
      }
    }"""


@pytest.fixture
def query_single_book():
    return """query {
      book(bookId: 1) {
        id
        title
        author
      }
    }"""


@pytest.mark.django_db
def test_book_list(graphql_client, books, query_all_books):
    response = graphql_client.execute(query_all_books)
    assert len(response["data"]["allBooks"]) == 3


@pytest.mark.django_db
def test_book_detail(graphql_client, single_book, query_single_book):
    response = graphql_client.execute(query_single_book)
    assert int(response["data"]["book"]["id"]) == single_book.id
    assert response["data"]["book"]["title"] == single_book.title


# @pytest.mark.django_db
# class TestMyModelData:
#     def test_none_response(self, graphql_client, query, my_model):
#         executed = graphql_client.execute(
#           query, variables={"searchParam": "skittles"}
#         )
#         assert executed == {"data": {"myModelData": None}}
#
#     def test_filters_usage(self, graphql_client, query, my_model):
#         params = {"searchParam": "skittles"}
#         executed = graphql_client.execute(query, variables=params)
#         assert executed == {"data": {"myModelData": {"totalCount": 20}}}
