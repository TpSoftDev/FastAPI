import random
from fastapi import FastAPI, HTTPException

# Initialize the FastAPI app
app = FastAPI()

# Create a sample database of books as a list of dictionaries
BOOK_DATABASE = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "ISBN": "978-0061120084"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "ISBN": "978-0451524935"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "year": 1925,
        "ISBN": "978-0743273565"
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "year": 1813,
        "ISBN": "978-1503290563"
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "year": 1951,
        "ISBN": "978-0316769488"
    },
    {
        "title": "Moby Dick",
        "author": "Herman Melville",
        "genre": "Adventure",
        "year": 1851,
        "ISBN": "978-1503280786"
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1954,
        "ISBN": "978-0618640157"
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1937,
        "ISBN": "978-0547928227"
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "genre": "Dystopian",
        "year": 1932,
        "ISBN": "978-0060850524"
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "genre": "Historical Fiction",
        "year": 1869,
        "ISBN": "978-0199232765"
    }
]

# Home endpoint - displays a welcome message
@app.get("/")
async def home():
    return {"Message": "Welcome To My BookStore!"}

# Endpoint to list all books in the database
@app.get("/list-books")
async def list_books():
    return {"Books": BOOK_DATABASE}

# Endpoint to get a book by its index in the list
@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    # Check if the index is within the range of the list
    if index < 0 or index >= len(BOOK_DATABASE):
        # If not, raise a 404 error with a custom message
        raise HTTPException(status_code=404, detail="Book not found")
    # If valid, return the book at the specified index
    return {"Book": BOOK_DATABASE[index]}

# Endpoint to get books by the author's name
@app.get("/book-by-author/{author}")
async def book_by_author(author: str):
    # Use list comprehension to find books with a matching author name (case-insensitive)
    books = [book for book in BOOK_DATABASE if book["author"].lower() == author.lower()]
    # If no books are found, raise a 404 error
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")
    # Return the list of books by the specified author
    return {"Books": books}

# Endpoint to get books by genre
@app.get("/book-by-genre/{genre}")
async def book_by_genre(genre: str):
    # Use list comprehension to find books with a matching genre (case-insensitive)
    books = [book for book in BOOK_DATABASE if book["genre"].lower() == genre.lower()]
    # If no books are found, raise a 404 error
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")
    # Return the list of books in the specified genre
    return {"Books": books}

# Endpoint to get books by the year they were published
@app.get("/book-by-year/{year}")
async def book_by_year(year: int):
    # Use list comprehension to find books published in the specified year
    books = [book for book in BOOK_DATABASE if book["year"] == year]
    # If no books are found, raise a 404 error
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")
    # Return the list of books published in the specified year
    return {"Books": books}

# Endpoint to get books by their ISBN number
@app.get("/book-by-isbn/{isbn}")
async def book_by_isbn(isbn: str):
    # Use list comprehension to find books with a matching ISBN
    books = [book for book in BOOK_DATABASE if book["ISBN"] == isbn]
    # If no books are found, raise a 404 error
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")
    # Return the book with the specified ISBN
    return {"Books": books}

# Endpoint to get books by their title
@app.get("/book-by-title/{title}")
async def book_by_title(title: str):
    # Use list comprehension to find books with a matching title (case-insensitive)
    books = [book for book in BOOK_DATABASE if book["title"].lower() == title.lower()]
    # If no books are found, raise a 404 error
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")
    # Return the book(s) with the specified title
    return {"Books": books}

@app.get("/get-random-book")
async def get_random_book():
    return random.choice(BOOK_DATABASE)


# /add-book

# /get-book?{} id =...
