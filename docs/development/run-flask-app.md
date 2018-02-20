# How to run the Flask application

This guide will show you how to run the Flask application for local development.

## Before you start

1. In the terminal, make sure you have activated your virtual environment:

  `source env/bin/activate`

2. Download the necessary packages:

  `pip install -r requirements.txt`

## Setup environment variables

1. Set these environment variables:

  `export FLASK_APP=manage.py` (tell Flask where the application is)

  `export FLASK_DEBUG=1` (automatically rebuild the app when code changes)

## Run Flask

1. To start the Flask app use the command `flask run`

2. In your browser, navigate to http://localhost:5000/


## Stopping the application

Use `control c` to stop the app.
