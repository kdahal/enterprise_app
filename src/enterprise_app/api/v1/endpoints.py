# src/enterprise_app/api/v1/endpoints.py
def health_check():
    return {"status": "ok"}