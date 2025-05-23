# Picker Wheel

A Django-based random decision maker with an interactive spinning wheel. This project allows users to create custom wheels with weighted options and beautiful animations.

## Features

- Create custom wheels with multiple options
- Set weights for each option
- Customize colors for wheel segments
- Smooth spinning animation
- Dark/Light theme support
- User authentication
- Mobile responsive design

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd picker-wheel
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to use the application.

## Usage

1. Register for an account or log in
2. Click "Create New Wheel" to start
3. Add items to your wheel with custom weights and colors
4. Save your wheel
5. Click "SPIN" to get a random result

## Technologies Used

- Python 3.8+
- Django 4.2
- HTML5 Canvas
- JavaScript (ES6+)
- Bootstrap 5
- CSS Custom Properties

## Contributing

Feel free to submit issues and enhancement requests! #   p i c k e r w h e e l  
 