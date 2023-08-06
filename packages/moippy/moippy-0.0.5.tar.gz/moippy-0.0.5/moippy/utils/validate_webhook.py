def IsValidWebhook(x_signature:str, body:bytes, secret:str):
    secret = secret.encode('utf-8')
    digest = hmac.HMAC(secret, body, hashlib.sha256).hexdigest()
    return digest == x_signature
