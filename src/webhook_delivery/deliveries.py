"""
Implements database operations for deliveries. 
Looks up status and attempt history, claims pending work, records outcomes, 
and recovers expired claims. Both the API and worker use this module.
"""