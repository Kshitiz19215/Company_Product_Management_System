# Company Product Management System

This Python-based web application manages company product data. The system comprises several components:

CreateCompany.py: Handles the creation of new companies, ensuring data integrity and generating tokens for secure requests.

DeleteCompany.py: Allows for the deletion of companies based on their unique IDs.

UpdateCompany.py: Provides functionality for updating company information, such as name, address, and country.

database.py: Manages database connections using MySQL.

Helper.py: Contains functions for token generation and validation.

config.py: Stores a secret key used for token generation.

Token folder: Contains two Python scripts for generating tokens, each using the secret key from config.py.

To run the application, ensure you have Flask and MySQL installed. Modify the database configuration in database.py. Run each component individually as a Flask application.

Description:
Manage company product data with this Python web app. Create, update, and delete companies securely using tokens. Includes database integration and token generation for authentication.
