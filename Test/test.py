# Importing FastAPI class from the fastapi module
from fastapi import FastAPI

# Creating an instance of the FastAPI class
app = FastAPI()

# Defining a route for the root URL "/"
@app.get("/")
# Asynchronous function to handle GET requests at the root URL
async def root():
    # Returning a JSON response with a message and a variable
    return {"message": "Hello World", "var": "1234"}




@app.get("/get-current-time")
async def get_current_time():
    return {"message": "The Current time is: 19:47PM"}

# API Endpoint
# Accessible at http://127.0.0.1:8000/
# get-current-time http://127.0.0.1:8000/

# Putting API EndPoint behind a domain
# Root PATH for the endpoint
# http://TpSoftDev.com