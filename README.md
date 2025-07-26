# DocuVector: PDF to SVG Converter

A Django web application that asynchronously converts vector-based PDF files to high-quality SVG using Celery and Redis. This project demonstrates a full-stack development cycle, from initial setup to production deployment.

**Live Demo:** [https://your-app-name.onrender.com](https://your-app-name.onrender.com) 
*(Note: The initial load might take up to a minute as the free instance on Render spins up from sleep.)*

![DocuVector Screenshot]() 

---

## Key Features

- **File Upload:** A user-friendly interface for uploading PDF documents.
- **Asynchronous Conversion:** Heavy processing tasks are handled in the background by Celery workers, ensuring the UI remains responsive.
- **Real-time Status Updates:** The frontend uses AJAX polling to dynamically update the conversion status without requiring a page refresh.
- **High-Quality Conversion:** Utilizes the `PyMuPDF` library to ensure accurate extraction of vector data and text from PDFs.
- **Production-Ready Setup:** The project is configured for deployment with Gunicorn, WhiteNoise, and environment variables for security.

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3 (Pico.css), JavaScript (AJAX/Fetch API)
- **Task Queue:** Celery
- **Message Broker:** Redis
- **Database:** PostgreSQL (in production), SQLite (in development)
- **Deployment:** Render, Gunicorn, WhiteNoise

---

## Local Development Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Andrii-Kon/DocuVector.git
    cd DocuVector
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the environment variables:**
    Create a `.env` file in the project root and add the following:
    ```
    SECRET_KEY='your-secret-key'
    DEBUG=True
    DATABASE_URL='sqlite:///db.sqlite3'
    REDIS_URL='redis://localhost:6379/0'
    ```

5.  **Run Redis.** Make sure you have a Redis server running on `localhost:6379`. You can use Docker or a local installation.

6.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Start the development server and Celery worker (in two separate terminals):**
    
    *Terminal 1: Django Server*
    ```bash
    python manage.py runserver
    ```
    *Terminal 2: Celery Worker*
    ```bash
    # On Windows (with gevent)
    celery -A config worker -l info -P gevent
    # On macOS/Linux
    celery -A config worker -l info
    ```

8.  Open your browser and navigate to `http://127.0.0.1:8000/`.
