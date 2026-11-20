"""
Creates the SQLAlchemy engine and session factory. 
The API uses a session per request that needs the database, 
and the worker opens sessions for its database operations.
"""