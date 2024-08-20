# Django REST API for E-Learning Platform

## Overview

This project is a Django REST API for an e-learning platform that includes functionality for user authentication, course management, cart and order processing, and more. It is built using Django, Django REST Framework, and integrates with Stripe and PayPal for payment processing.

## Features

- User authentication with JWT
- User registration and password management
- Course listing and details
- Cart management and checkout
- Order creation and payment processing
- Coupon application
- Student profile and progress tracking
- Note-taking and course reviews

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL or any other database supported by Django

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
2. **Create and activate a virtual environment:**

   ```bash
      python -m venv venv
      source venv/bin/activate   On Windows use venv\Scripts\activate

3. **Install the required packages:**

   ```bash
      pip install -r requirements.txt

4. **Set up your environment variables:**
   ```bash

      SECRET_KEY=your_secret_key
      DEBUG=True
      DATABASE_URL=your_database_url
      STRIPE_SECRET_KEY=your_stripe_secret_key
      PAYPAL_CLIENT_ID=your_paypal_client_id
      PAYPAL_SECRET_ID=your_paypal_secret_id
      FRONTEND_SITE_URL=your_frontend_url

5. **Run database migrations:**

    ```bash
    python manage.py migrate

6. **Run the development server:**

    ```bash
    python manage.py runserver
