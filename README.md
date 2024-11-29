# Product API
This project implements a simple REST API using FastAPI to manage products. Each product has a name, description, and price.

# SETUP
One needs to have installed a python version and pip

# Creating a virtual environment
`python -m venv .venv`
`.\.venv\Scripts\Activate.ps1`

# Installation
Installed FastAPI and Uvicorn 
`pip install fastapi uvicorn`

# Start the API server
`python -m uvicorn main:app --reload`

I then created a new product, which my API was supposed to get, and be displayed in the browser, from the server http://127.0.0.1:8000

# Install requests
`pip install requests`
`pip show requests`

# Run the client script. The script will add a sample product and then retrieve the list of products.
`python client.py`