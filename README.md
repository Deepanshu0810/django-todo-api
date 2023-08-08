# django-todo-api
This project is built to demonstrate the application of Django Rest Framework by creating a To-Do web app

## What is REST?
REST stands for Representational State Transfer. It is a software architectural style that defines a set of constraints to be used for creating Web services. Web services that conform to the REST architectural style, called RESTful Web services, provide interoperability between computer systems on the Internet. RESTful Web services allow the requesting systems to access and manipulate textual representations of Web resources by using a uniform and predefined set of stateless operations.

### Understanding Representation
A representation is a sequence of bytes, plus representation metadata to describe those bytes. Other commonly used but less precise names for a representation include: document, file, and HTTP message entity, instance, or variant.

### Understanding State Transfer
The client-server communication is constrained by no client context being stored on the server between requests. Each request from any client contains all the information necessary to service the request, and session state is held in the client. The session state can be transferred by the server to another service such as a database to maintain a persistent state for a period and allow authentication. The client begins sending requests when it is ready to make the transition to a new state. While one or more requests are outstanding, the client is considered to be in transition. The representation of each application state contains links that may be used the next time the client chooses to initiate a new state-transition.

## About the Project
This project is built to demonstrate the application of Django Rest Framework by creating a To-Do web app. The project is built using Django Rest Framework and SQLite database.

### Environment Setup
```bash
# Create a virtual environment
conda create -p env python

# Activate the virtual environment
conda activate env/

# Install the dependencies
pip install -r requirements.txt
```

### Django Setup
```bash
django-admin startproject todo_api
cd todo_api
python manage.py startapp api
```