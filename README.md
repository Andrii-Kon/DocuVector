# DocuVector: PDF to SVG Converter

A Django web application that asynchronously converts vector-based PDF files to high-quality SVG using Celery and Redis. This project demonstrates a full-stack development cycle, from initial setup and local development to production deployment on a cloud platform.

**Live Demo:** [https://docuvector.onrender.com/](https://docuvector.onrender.com/)

*(**Note:** The initial load might take up to a minute as the free instance on Render spins up from sleep. Additionally, due to free tier limitations, the background worker is not active in this live demo. The file conversion will remain in the 'Processing' state. However, the application is fully configured for asynchronous task processing, as can be seen in the source code.)*

---

![Анімація](https://github.com/user-attachments/assets/e4cc410d-edda-4e44-8ed9-a72a1d5fffd7)

---

## Key Features

- **File Upload:** A clean, user-friendly interface for uploading PDF documents.
- **Asynchronous Architecture:** Heavy processing tasks are designed to be handled by Celery workers, ensuring the UI remains responsive even with large files.
- **Real-time Status Updates:** The frontend uses AJAX polling to dynamically update the conversion status without requiring a page refresh.
- **High-Quality Conversion:** Utilizes the `PyMuPDF` library to ensure accurate extraction of vector data and text from PDFs.
- **Production-Ready Setup:** The project is configured for deployment with Gunicorn, WhiteNoise, PostgreSQL, and environment variables for security.

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3 (Pico.css), JavaScript (AJAX/Fetch API)
- **Task Queue:** Celery
- **Message Broker & Cache:** Redis
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

5.  **Run Redis.** Make sure you have a Redis server running on `localhost:6379`.

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
