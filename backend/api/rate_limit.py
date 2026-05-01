import time

REQUESTS = {}

def rate_limit(client_id: str):
    now = time.time()
    window = 60

    if client_id not in REQUESTS:
        REQUESTS[client_id] = []

    REQUESTS[client_id] = [
        t for t in REQUESTS[client_id] if now - t < window
    ]

    if len(REQUESTS[client_id]) >= 100:
        return False

    REQUESTS[client_id].append(now)
    return True