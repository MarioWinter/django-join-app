# Join API

## Overview

A simple API for the Kanban WebApp Join.

## Version

-   **Version**: 1.0.0

## Authentication

### User Login

-   **POST** `/api/auth/login/`
    -   **Description**: CustomLoginView is a subclass of ObtainAuthToken that handles user login.
    -   **Request Body**:
        -   `username`: The username of the user.
        -   `password`: The password of the user.
    -   **Responses**:
        -   `200 OK`: Returns the authentication token, username, user ID, and email.
    -   **Security**: Token-based authentication.

### User Registration

-   **POST** `/api/auth/registration/`
    -   **Description**: Handles user registration.
    -   **Request Body**:
        -   `username`: The username of the new user.
        -   `email`: The email address of the new user.
        -   `password`: The password of the new user.
    -   **Responses**:
        -   `200 OK`: Returns the authentication token, username, user ID, email, and background color.
    -   **Security**: Token-based authentication.

## Contacts

### List Contacts

-   **GET** `/api/v1/contacts/`
    -   **Description**: A viewset for viewing and editing contact instances.
    -   **Responses**:
        -   `200 OK`: Returns a list of contact objects in JSON format.
    -   **Security**: Token-based authentication.

### Create Contact

-   **POST** `/api/v1/contacts/`
    -   **Description**: A viewset for creating contact instances.
    -   **Request Body**:
        -   `name`: The name of the contact.
        -   `email`: The email address of the contact.
        -   `phone`: The phone number of the contact.
    -   **Responses**:
        -   `201 Created`: Returns the created contact object in JSON format.
    -   **Security**: Token-based authentication.

### Retrieve Contact

-   **GET** `/api/v1/contacts/{id}/`
    -   **Description**: Retrieves details of a specific contact by ID.
    -   **Parameters**:
        -   `id`: A unique integer value identifying this contact.
    -   **Responses**:
        -   `200 OK`: Returns the contact object in JSON format.
    -   **Security**: Token-based authentication.

### Update Contact

-   **PUT** `/api/v1/contacts/{id}/`
    -   **Description**: Updates an existing contact by ID.
    -   **Request Body**: (Similar to creating)
    -   **Responses**:
        -   `200 OK`: Returns the updated contact object in JSON format.
    -   **Security**: Token-based authentication.

### Delete Contact

-   **DELETE** `/api/v1/contacts/{id}/`
    -   **Description**: Deletes a specific contact by ID.
    -   **Parameters**:
        -   `id`: A unique integer value identifying this contact.
    -   **Responses**:
        -   `204 No Content`: Confirms that the contact was successfully deleted.
    -   **Security**: Token-based authentication.

## User Profile

### Retrieve User Profile

-   **GET** `/api/v1/profile/`
    -   **Description**: Retrieves the profile of the current user.
    -   **Responses**:
        -   `200 OK`: Returns the user profile object in JSON format.
    -   **Security**: Token-based authentication.

### Update User Profile

-   **PUT** `/api/v1/profile/{id}/`
    -   **Description**: Updates a specific user's profile by ID.
    -   **Request Body**: (Similar to creating)
    -   **Responses**:
        -   `200 OK`: Returns the updated user profile object in JSON format.
    -   **Security**: Token-based authentication.

## Tasks

### List Tasks

-   **GET** `/api/v1/tasks/`
    -   **Description**: Retrieves a list of tasks for the current user.
    -   **Responses**:
        -   `200 OK`: Returns a list of task objects in JSON format.
    -   **Security**: Token-based authentication.

### Create Task

-   **POST** `/api/v1/tasks/`
    -   **Description**: Creates a new task for the current user.
    -   **Request Body**:
        -   `title`: The title of the task.
        -   `description`: A description of the task (optional).
        -   `due_date`: The due date for the task (optional).
    -   **Responses**:
        -   `201 Created`: Returns the created task object in JSON format.
    -   **Security**: Token-based authentication.

### Retrieve Task

-   **GET** `/api/v1/tasks/{id}/`
    -   **Description**: Retrieves details of a specific task by ID.
    -   **Parameters**:
        -   `id`: A unique integer value identifying this task.
    -   **Responses**:
        -   `200 OK`: Returns the task object in JSON format.
    -   **Security**: Token-based authentication.

### Update Task

-   **PUT** `/api/v1/tasks/{id}/`
    -   **Description**: Updates an existing task by ID.
    -   **Request Body**: (Similar to creating)
    -   **Responses**:
        -   `200 OK`: Returns the updated task object in JSON format.
    -   **Security**: Token-based authentication.

## Security

The API uses token-based authentication. Ensure to include a valid token in your request headers:
