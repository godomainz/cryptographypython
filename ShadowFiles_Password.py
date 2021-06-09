import hashlib
import base64
import string

def guess_password(salt, iterations, entropy):
    alphabet = string.ascii_lowercase
    for c1 in alphabet:
        for c2 in alphabet:
            password = str.encode(c1 + c2)
            value = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128))
            if value == entropy:
                return password
    return "".encode()

iterations = 1 #45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
validation = "SALTED-SHA512-PBKDF2"
entropy = "Kp64cWBoPly+4a+X6sIocmsYGM51a06+oNUaXR+avGHvIp8HzrArgsM5DTRQDppoeeaU59SJHZq7SYPESsXVIpAlXt5M4+bIfgYvg0Imu9mHBA4DDV7hnYFr3z/3iWgs6pKT1uMESDXZaBah1tZykKsZEWczAHwZ4irW4mexmJs=".encode()

password = "??".encode()
password = guess_password(salt, iterations, entropy)
print(password)
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
print(value)
print(entropy)
