"""
Creates the FastAPI app and defines the routes. 
POST `/events` calls the event logic, GET `/deliveries/{id}` looks up delivery status, 
and GET `/healthz` checks that the API responds.
"""
from fastapi import FastAPI

app = FastAPI(title="Webhook Delivery Service")


"""Health check.

Usage: 
  curl http://localhost:8000/healthz
"""
@app.get("/healthz")
def healthz() -> dict[str, str]:
  return {"status": "ok"}