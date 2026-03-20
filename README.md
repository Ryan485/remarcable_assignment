# Remarcable Take-home Assingment - Ryan Song
## Project description
This application allows users to search and filter electrical materials products by description, category, and tags. It demonstrates proficiency in Django by implementing models with appropriate relationships, a functional search and filter system, and a clean admin interface for data management.

## Requirements
- **Language:** Python 3.12+ (Tested on 3.12.x)
- **Framework:** Django 6.0.3
- **Database:** SQLite (included with Python)

## Setup instructions
1. **Clone repository** at https://github.com/Ryan485/remarcable_assignment.git

2. **Set up venv environment** 
```bash
cd remarcable_assignment

python3 -m venv venv

source venv/bin/activate
```

3. **Install Django**
```bash
pip install django
```

4. **Run Migration**
```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
```

5. **Create a superuser** (optional, only needed for admin access at `/admin/`)
```bash
    python3 manage.py createsuperuser
```

6. **Load sample data**
```bash
    python3 manage.py loaddata fixtures.json
```

7. **Run the server**
```bash
    python3 manage.py runserver
```

8. **Visit** `http://127.0.0.1:8000/products/` to use the application.

## AI Usage Note
Claude was used as a reference tool during development — primarily 
for clarifying Django concepts and best practices. All code was written and 
understood by me, and I am able to explain every part of the implementation.