"""
Implements event submission. 
Creates the event and its pending delivery in one transaction. 
Handles repeated idempotency keys so the same submission returns the original IDs.
"""