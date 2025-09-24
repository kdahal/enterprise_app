# # src/enterprise_app/api/v1/endpoints.py
# def health_check():
#     return {"status": "ok"}

# using FastAPI, update endpoints.py to include actual routes and test them with httpx:
# src/enterprise_app/api/v1/endpoints.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}
