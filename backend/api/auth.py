from fastapi import Header, HTTPException
import jwt

API_KEY = "secret-api-key"

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True


def verify_jwt(authorization: str = Header(None)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, "SECRET", algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=403, detail="Invalid JWT")