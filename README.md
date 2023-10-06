# slooviassignment

# Flask Registration and Template Management App

This is a simple Flask web application that provides user registration and template management features using a MongoDB database for data storage. Users can register, log in, create, update, and delete templates. JWT authentication is used to secure the template management functionality.

## Prerequisites

Before you begin, ensure you have the following requirements installed:

- Python 3.x
- Flask
- Flask-PyMongo
- Flask-JWT-Extended
- pymongo

You can install these dependencies using `pip`:

    ```bash
    pip install Flask Flask-PyMongo Flask-JWT-Extended pymongo

# Setup

1.Clone the repository to your local machine:

    ```bash
    git clone https://github.com/praa532/slooviassignment.git
    cd slooviassignment

1. Configure the MongoDB connection:

- Open the app.py file.

- Update the MONGO_URI in the app.py file with your MongoDB connection URI and database name.

2. Run the Flask app:

        ```bash
        python app.py

The app will start on http://localhost:5000/.

#Usage

#User Registration

1. Access the registration page by going to http://localhost:5000/register in your web browser.

2. Fill out the registration form with your details, including first name, last name, email, and password.

3. Click the "Register" button to create your account.

# User Login

1. Access the login page by going to http://localhost:5000/login in your web browser.

2. Enter your registered email and password.

2. Click the "Login" button to log in.

# Template Management

1. After logging in, you can access the template management features.

2. Create a new template by providing a template name, subject, and body.

3. View all templates, including those created by you.

4. View details of a specific template by clicking on its name.

5. Edit a template by clicking the "Edit" button on the template details page.

6. Delete a template by clicking the "Delete" button on the template details page.

# API Endpoints

The app also provides the following API endpoints for template management:

- POST /template - Create a new template (requires authentication).
- GET /template - Get all templates (requires authentication).
- GET /template/<template_id> - Get a specific template by ID (requires authentication).
- PUT /template/<template_id> - Update a specific template by ID (requires authentication).
- DELETE /template/<template_id> - Delete a specific template by ID (requires authentication).

# License

This project is licensed under the MIT License - see the LICENSE file for details.


You can save this content as a `README.md` file in the root directory of your Flask app repository. Make sure to replace placeholders like `yourusername` and update the MongoDB connection URI with your actual values. This README file provides clear instructions on how to set up and use your Flask app.
