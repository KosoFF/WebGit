"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from WebGit import app
from os import environ




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
