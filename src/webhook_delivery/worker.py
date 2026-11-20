"""
Runs the background loop. 
Claims a delivery, sends the webhook with HTTPX, applies the retry policy, and saves the result. 
The HTTP request runs outside the database transaction used to claim work.
"""