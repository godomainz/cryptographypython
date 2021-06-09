import hashlib

# Alice and Bob has shared secret key
secret_key = "secret key".encode()

# Alice wants to compute a MAC
m = "Hey Bob, You are still awesome".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()

print(m, hmac)

# Bob recieves and validates the HMAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
print(m, hmac)