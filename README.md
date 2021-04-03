# Demo graphql project

## Resources
* https://www.twilio.com/blog/graphql-apis-django-graphene
* https://morningpython.com/2019/12/23/unit-testing-graphene-django-api-with-pytest/


## Queries

Select all books

    query {
      allBooks {
        id
        title
        author
        yearPublished
        review
      }
    }

Select a specific book

    query {
      book(bookId: 2) {
        id
        title
        author
      }
    }

Filtered search (ex. 1)

    {
      allBooks(yearPublished: "1974", title_Icontains: "Mecano", review: 10) {
        edges {
          node {
            title
            author
            yearPublished
            review
          }
        }
      }
    }

Filtered search (ex. 2)
 
    {
      allBooks(yearPublished: "2002", title: "Atomic") {
        edges {
          node {
            title
            author
            yearPublished
            review
          }
        }
      }
    }

Creating a book

    mutation createMutation {
      createBook(bookData: {title: "Things Apart", author: "Chinua Achebe", yearPublished: "1985", review: 3}) {
        book {
          title,
          author,
          yearPublished,
          review
        }
      }
    }

Updating an existing book

    mutation updateMutation {
      updateBook(bookData: {id: 6, title: "Things Fall Apart", author: "Chinua Achebe", yearPublished: "1958", review: 5}) {
        book {
          title,
          author,
          yearPublished,
          review
        }
      }
    }

Deleting a book

    mutation deleteMutation{
      deleteBook(id: 6) {
        book {
          id
        } 
      }
    }


