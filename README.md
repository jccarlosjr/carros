# Project Cars

The **Cars** project is a web application built with Django that allows users to create an account and, after logging in, list, create, edit and delete car listings.

## Features

- **Create a User**: Allows the creation of new user accounts.
- **List Cars**: Logged-in users can view a list of available cars.
- **Create a Car Ad**: Logged-in users can create new car ads.
- **Edit a Car Ad**: Logged-in users can edit their existing ads.
- **Delete a Car Ad**: Logged-in users can delete their existing ads.


## Requirements

Make sure you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/) installed.

## Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/yourusername/cars.git](https://github.com/jccarlosjr/cars.git)
    ```


2. Navigate to the project directory:

    ```bash
    cd cars
    ```


3. Create and activate a virtual environment (optional, but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the migrations:

    ```bash
    python manage.py migrate
    ```



6. Create a superuser to access the admin panel (optional):

    ```bash
    python manage.py createsuperuser
    ```


7. Start the development server:

    ```bash
    python manage.py runserver
    ```
    
    The server will be available at `http://127.0.0.1:8000/`.

## Usage

1. Go to the app home page and register a new account or log in with an existing account.
2. After logging in, you can list, create, edit, and delete car ads.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

