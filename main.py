import json
import os
import random
from typing import Optional, List
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


# Initialize the FastAPI app
app = FastAPI()

# Book Model
class Book(BaseModel):
    title: str
    author: str
    genre: str
    year: Optional[int] = None
    ISBN: Optional[int] = None
    book_id: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)
        if not self.book_id:
            self.book_id = uuid4().hex


BOOKS_FILE = 'books.json'

# Load existing books from file if available
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as f:
            return json.load(f)
    return []

BOOK_DATABASE = load_books()

# Save books to file
def save_books():
    with open(BOOKS_FILE, 'w') as f:
        json.dump(BOOK_DATABASE, f, indent=4)

# Home endpoint - displays a welcome message
@app.get("/")
async def home():
    return {"Message": "Welcome to My BookStore!"}

# List all books
@app.get("/list-books")
async def list_books():
    return {"Books": BOOK_DATABASE}

# Get a book by its index
@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if not (0 <= index < len(BOOK_DATABASE)):
        raise HTTPException(status_code=404, detail=f"Index {index} is out of range.")
    return {"Book": BOOK_DATABASE[index]}

# Get books by author
@app.get("/book-by-author/{author}")
async def book_by_author(author: str):
    books = [book for book in BOOK_DATABASE if book["author"].lower() == author.lower()]
    if not books:
        raise HTTPException(status_code=404, detail="No books found by this author.")
    return {"Books": books}

# Get books by genre
@app.get("/book-by-genre/{genre}")
async def book_by_genre(genre: str):
    books = [book for book in BOOK_DATABASE if book["genre"].lower() == genre.lower()]
    if not books:
        raise HTTPException(status_code=404, detail="No books found in this genre.")
    return {"Books": books}

# Get books by publication year
@app.get("/book-by-year/{year}")
async def book_by_year(year: int):
    books = [book for book in BOOK_DATABASE if book["year"] == year]
    if not books:
        raise HTTPException(status_code=404, detail="No books found from this year.")
    return {"Books": books}

# Get books by ISBN
@app.get("/book-by-isbn/{isbn}")
async def book_by_isbn(isbn: int):
    books = [book for book in BOOK_DATABASE if book["ISBN"] == isbn]
    if not books:
        raise HTTPException(status_code=404, detail="No books found with this ISBN.")
    return {"Books": books}

# Get books by title
@app.get("/book-by-title/{title}")
async def book_by_title(title: str):
    books = [book for book in BOOK_DATABASE if book["title"].lower() == title.lower()]
    if not books:
        raise HTTPException(status_code=404, detail="No books found with this title.")
    return {"Books": books}

# Get a random book
@app.get("/get-random-book")
async def get_random_book():
    if not BOOK_DATABASE:
        raise HTTPException(status_code=404, detail="No books available.")
    return random.choice(BOOK_DATABASE)

# Add a new book
@app.post("/add-book")
async def add_book(book: Book):
    json_book = jsonable_encoder(book)
    BOOK_DATABASE.append(json_book)
    save_books()
    return {"Message": f"Book '{book.title}' was successfully added.", "book_id": book.book_id}

# Get a book by its ID
@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOK_DATABASE:
        if book["book_id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found.")