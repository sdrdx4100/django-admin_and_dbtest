# django-admin_and_dbtest

## Setting up a Python virtual environment

To set up a Python virtual environment, follow these steps:

1. Create a virtual environment using `venv`:
   ```sh
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

3. Install dependencies using `pip`:
   ```sh
   pip install -r requirements.txt
   ```

## Creating a Django Project

To create a Django project, follow these steps:

1. Install Django in your virtual environment:
   ```sh
   pip install django
   ```

2. Create a new Django project:
   ```sh
   django-admin startproject project_name
   ```

## Running the Django Server

To run the Django server, follow these steps:

1. Navigate to the project directory:
   ```sh
   cd project_name
   ```

2. Run the Django development server:
   ```sh
   python manage.py runserver
   ```

3. Open your web browser and go to `http://127.0.0.1:8000/` to see the Django welcome page.
