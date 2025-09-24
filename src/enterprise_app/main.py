# Application entry poin
# Using FastAPI, Update main.py to include the router:
# src/enterprise_app/main.py
from fastapi import FastAPI
from enterprise_app.api.v1.endpoints import router

app = FastAPI()
app.include_router(router, prefix="/api/v1")