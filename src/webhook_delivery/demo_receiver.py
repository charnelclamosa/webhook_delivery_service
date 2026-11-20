"""
Defines a small FastAPI app that acts as the receiving system. 
It can return 503 on the first request for a delivery ID and 200 on the next, 
so you can demonstrate a successful retry.
"""