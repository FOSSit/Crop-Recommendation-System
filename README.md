# Crop Prediction

Crop Prediction is a project aimed at developing a predictive model and website for assisting farmers in making informed decisions about crop selection based on various factors such as soil type, climate conditions, and historical crop data.

## Project Overview

The project utilizes the Django web framework for backend development and SQLite database for storing crop and user data.

### Key Technologies

- Django Framework
- SQLite Database

## Installation Guide

### System Requirements

- Python 3.x
- pip package manager

### Dependency Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/your-username/crop-prediction.git
cd crop-prediction
```

2. Create a virtual environment:

```bash
# For macOS/Linux
python3 -m venv venv

# For Windows
python -m venv venv
```

3. Activate the virtual environment:

```bash
# For macOS/Linux
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

### Platform-Specific Instructions

- For Windows: Replace `source` with `.\venv\Scripts\activate`

## Usage Guide

To run the website locally, use the following command:

```bash
python manage.py runserver
```

This command will start the development server, and you can access the website at `http://localhost:8000` in your web browser.
