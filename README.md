# Library API

The Library API is a Flask-based web service that allows users to manage a library system. It provides various endpoints for user registration, authentication, book management, and retrieving book information.

## Features

- **User Registration:** Users can create a new account by providing their personal information, such as name, username, email, password, and gender.
- **User Authentication:** Users can log in to their account using their username and password. Authentication is implemented using JWT (JSON Web Tokens) for secure access to protected routes.
- **Book Management:** Users with the appropriate authentication can add new books to the library, edit existing book details, delete books, and retrieve a list of all available books.
- **Book Information:** Users can view detailed information about a specific book, including its title, author, ISBN, publisher, publication year, genre, synopsis, language, page count, cover image, inventory count, and available count.

## Technology Stack

The Library API is built using the following technologies:

- **Python:** The core programming language for implementing the API logic.
- **Flask:** A lightweight web framework used to create the API endpoints and handle HTTP requests.
- **SQLAlchemy:** A Python SQL toolkit and ORM (Object-Relational Mapping) library for interacting with the SQLite database.
- **Marshmallow:** A serialization library used for defining object schemas and converting Python objects to JSON.
- **Flask-JWT-Extended:** A Flask extension for JWT-based authentication and token management.
- **Flask-Mail:** A Flask extension for sending emails.

## Getting Started

To set up and run the Library API locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/library-api.git

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set up the database:**
- Run the following CLI command to create the database:
  ```
  flask db_create
  ```

- (Optional) Run the following CLI command to seed the database with sample data:
  ```
  flask db_seed
  ```

4. **Start the API server:**
  ```
  flask run
  ```


The API server will start running locally at `http://localhost:5000`. You can now make HTTP requests to the available endpoints using a tool like cURL or an API client like Postman.

Please note that additional configuration, such as setting up the mail server, may be required depending on your specific needs.

Feel free to explore the API endpoints and customize the code according to your requirements.
