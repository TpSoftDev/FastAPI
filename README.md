# Book Management API

## Overview

This repository contains a FastAPI-based book management system designed to handle book-related operations such as listing, searching, adding, and retrieving books. The API is built using modern Python technologies and follows industry standards for web development and API design.

## Features

- **CRUD Operations**: Create, read, update, and delete books in the system.
- **Search Capabilities**: Find books by title, author, genre, publication year, or ISBN.
- **Random Book Retrieval**: Retrieve a random book from the collection.
- **Book Identification**: Each book is assigned a unique ID for easy retrieval.

## Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **JSON**: Data interchange format for storing and retrieving book information.
- **UUID**: For generating unique IDs for books.
- **Python Typing**: Optional and list types for improved code readability and type safety.

## API Endpoints

### Home

- **GET** `/`
  - Returns a welcome message.

### List Books

- **GET** `/list-books`
  - Lists all books in the database.

### Book Operations

- **GET** `/book-by-index/{index}`
  - Retrieves a book by its index.
- **GET** `/book-by-author/{author}`
  - Retrieves books by author.
- **GET** `/book-by-genre/{genre}`
  - Retrieves books by genre.
- **GET** `/book-by-year/{year}`
  - Retrieves books by publication year.
- **GET** `/book-by-isbn/{isbn}`
  - Retrieves books by ISBN.
- **GET** `/book-by-title/{title}`
  - Retrieves books by title.
- **GET** `/get-random-book`
  - Retrieves a random book from the database.
- **POST** `/add-book`
  - Adds a new book to the database.
- **GET** `/get-book`
  - Retrieves a book by its unique ID.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/book-management-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd book-management-api
   ```

3. Install the required packages:

   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## Code Structure

- `main.py`: Contains the FastAPI application, route definitions, and logic for managing books.
- `books.json`: Persistent storage for book data.

## Skills Demonstrated

- **FastAPI Development**: Building RESTful APIs with FastAPI, leveraging asynchronous features for performance.
- **Data Modeling**: Using Pydantic for data validation and serialization.
- **File Handling**: Managing JSON files for data persistence.
- **Error Handling**: Implementing proper error responses using HTTPException.
- **UUID Generation**: Ensuring unique book identifiers.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes or enhancements, please open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) - For providing a modern framework for building APIs.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - For data validation and settings management.
