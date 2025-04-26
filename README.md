# Simple Info Website - Django Project

A small Django web application that displays quotes and FAQs on separate pages. Built as part of a student project to demonstrate basic Django concepts including models, views, templates, and admin functionality.

## Features

- Two models: Quote and FAQ
- Two separate pages to display content:
  - Home page showing quotes
  - About page showing FAQs
- Django admin integration for content management
- Clean templates with basic styling
- Proper URL routing with namespaces

## Project Structure

```
simple_info_site/
├── .venv/                  # Virtual environment
├── studentproject/         # Main project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py
├── info/                   # App folder
│   ├── migrations/         # Database migrations
│   ├── __init__.py
│   ├── admin.py            # Admin panel configuration
│   ├── apps.py
│   ├── models.py           # Quote and FAQ models
│   ├── tests.py
│   ├── urls.py             # App URL configuration
│   └── views.py            # View functions
├── info/templates/         # Templates folder
│   └── info/
│       ├── home.html       # Home page template
│       └── about.html      # About page template
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── README.md               # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-info-site.git
   cd simple-info-site
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   
   # On Windows:
   .\.venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install django
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

### Admin Panel

1. Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
2. Log in with your superuser credentials
3. Add, edit, or delete Quotes and FAQs

### Viewing Content

- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see all quotes
- Visit [http://127.0.0.1:8000/about/](http://127.0.0.1:8000/about/) to see all FAQs

## Learning Objectives

This project demonstrates:

- Creating and configuring a Django project
- Defining models and migrations
- Implementing views and templates
- Using the Django admin interface
- Setting up URL patterns with namespaces
- Using Django Template Language (DTL)
- Basic front-end styling

## License

This project is for educational purposes. Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
