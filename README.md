# Demo graphql project

## Tutorial from Twilio
https://www.twilio.com/blog/graphql-apis-django-graphene


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


