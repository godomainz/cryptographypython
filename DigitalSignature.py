import hashlib


# These are Alices's RSA keys
# Public key (e,n) 5 11757331
# Secret key (d) 783365
n = 11757331
e = 5
d = 783365

# This is the message that Alice wants to sign ans send to Bob
message = "Bob you are awesome"

# Step 1: Hash the message
sha256 = hashlib.sha256()
sha256.update(message.encode())
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value :", h)

# Step 2: decrypt the hash value (use secret exponent)
sign = (h**d) % n

# Step 3: send message with signature to Bob
print(message, sign)

# Bob verifying the signature

# Step 1: Calculate the Hash value
sha256 = hashlib.sha256()
sha256.update(message.encode())
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value :", h)

# Step 2: verify the signature
verification = (sign**e) % n
print("Verification :", verification)