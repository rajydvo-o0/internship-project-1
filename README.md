# Simple E-commerce Store

A clean and responsive e-commerce web application built using Django, HTML, CSS, and JavaScript. The project provides essential online shopping functionality with a modern user interface and secure user authentication.

## Features

- User Registration & Login
- Product Listing
- Product Details
- Shopping Cart
- Order Processing
- Responsive Design

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

## Project Structure

```
ecommerce-store/
│── ecommerce/          # Django project settings
│── store/              # Main application
│── templates/          # HTML templates
│── static/             # CSS, JavaScript, Images
│── media/              # Uploaded media
│── manage.py
│── requirements.txt
```

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ecommerce-store.git

# Navigate to the project
cd ecommerce-store

# Create virtual environment
python -m venv venv

# Activate virtual environment

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Author

**Rajeshvar Yadav**
