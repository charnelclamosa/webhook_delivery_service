"""
Decides whether a failure is retryable and how long to wait. 
For example, a 503 can schedule another attempt, 
a 400 ends the delivery, and the attempt limit caps retries. 
NOTE: Keep this as plain Python so I can test it without PostgreSQL or a running API.
"""