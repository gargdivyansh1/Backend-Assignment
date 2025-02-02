# Backend-Assignment

# Multilingual FAQ API
## AI is used for writing the better commit text, comments and also helped in writing the README.md file.

## Overview
This project is a **Multilingual FAQ API** built using **Django and Django REST Framework (DRF)**. It allows users to retrieve frequently asked questions (FAQs) in multiple languages, leveraging **Google Translate API** and caching for efficiency. The system also integrates **django-ckeditor** for a rich text editing experience in the Django admin panel.

## Features
- **Multilingual Support**: Retrieve FAQs in different languages (`English`, `Hindi`, `Bengali`).
- **WYSIWYG Editor**: Use `django-ckeditor` for rich-text answers.
- **REST API**: Fetch FAQs via a simple API request.
- **Caching with Redis**: Enhances performance by storing translated FAQs.
- **Django Admin Integration**: Easily manage FAQs via the Django admin panel.
- **Automated Translation**: Uses `googletrans` to translate FAQs dynamically.
- **PEP8 Compliant Code**: Follows best practices for maintainability.

---

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Django 5+
- Redis (for caching)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/multilingual-faq.git
   cd multilingual-faq
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Start Redis server:**
   ```bash
   redis-server
   ```

---

## API Endpoints
### Get FAQs
- **Endpoint:** `/api/faqs/`
- **Method:** `GET`
- **Query Parameter:** `lang` (default: `en`)
- **Example Requests:**
  ```bash
  curl -X GET http://127.0.0.1:8000/api/faqs/
  curl -X GET http://127.0.0.1:8000/api/faqs/?lang=hi
  curl -X GET http://127.0.0.1:8000/api/faqs/?lang=bn
  ```

- **Example Response:**
  ```json
  [
    {
      "question": "What is Django?",
      "answer": "Django is a web framework."
    }
  ]
  ```

---

## Admin Panel
- **Access URL:** `http://127.0.0.1:8000/admin/`
- **Manage FAQs:** Add, update, or delete FAQs with translations.

---

## Technologies Used
- **Django** (Backend framework)
- **Django REST Framework** (API development)
- **Redis** (Caching layer)
- **Google Translate API (`googletrans`)** (Automatic translation)
- **django-ckeditor** (Rich text editor for answers)

---

## Running Tests
Run the unit tests to verify the functionality:
```bash
python manage.py test
```

---

## Author
- **Divyansh Garg**
- **Email: divyanshgarg515@gmail.com**
- **GitHub: gargdivyansh1(https://github.com/divyanshgarg1)**
