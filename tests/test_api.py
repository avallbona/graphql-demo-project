import pytest
from graphene.test import Client
from graphql_relay import to_global_id


@pytest.fixture
def query_all_books():
    return """{
      allBooks {
        edges {
          node {
            id
            title
            author
            yearPublished
            review
          }
        }
      }
    }"""


@pytest.fixture
def query_all_books_filtered():
    return """query($yearPublished:String!){
      allBooks($yearPublished:String){
        edges {
          node {
            id
            title
            author
            yearPublished
            review
          }
        }
      }
    }"""


@pytest.fixture
def query_single_book():
    return """query($id:ID!)
    {
        book(id:$id) {
            id
            title
            author
            yearPublished
            review
        }
    }
    """


@pytest.fixture
def mutation_book_create():
    return """
     mutation CreateBlog($input: BlogInputType!) {
        createBlog(input: $input) {
            blog {
                id
                title
                author {
                    id
                    name
                }
            }
            ok
        }
    }"""


@pytest.mark.django_db
def test_book_list(graphql_client: Client, books, query_all_books):
    response = graphql_client.execute(query_all_books)
    assert len(response["data"]["allBooks"]["edges"]) == 5
    first_passed = books[0]
    first_ret = response["data"]["allBooks"]["edges"][0]["node"]
    assert first_passed.title == first_ret.get("title")
    assert first_passed.author == first_ret.get("author")


@pytest.mark.django_db
def test_book_list_filtered_with_results(
    graphql_client: Client, books, query_all_books_filtered
):
    response = graphql_client.execute(
        query_all_books_filtered, variables={"yearPublished": "2021"}
    )
    assert len(response["data"]["allBooks"]["edges"]) == 2
    first_passed = books[0]
    first_ret = response["data"]["allBooks"]["edges"][0]["node"]
    assert first_passed.title == first_ret.get("title")
    assert first_passed.author == first_ret.get("author")


@pytest.mark.django_db
def test_book_detail(graphql_client, single_book, query_single_book):

    global_id = to_global_id("BookType", single_book.id)
    variables = {"id": global_id}

    response = graphql_client.execute(
        query_single_book,
        op_name="book",
        variables=variables,
    )
    assert response["data"]["book"]["id"] == global_id
    assert response["data"]["book"]["title"] == single_book.title


# def test_some_query(client_query):
#     response = client_query(
#         """
#         query {
#             myModel {
#                 id
#                 name
#             }
#         }
#         """,
#         op_name="myModel",
#     )
#
#     content = json.loads(response.content)
#     assert "errors" not in content


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
