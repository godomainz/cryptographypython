import string


def generate_key(n):
    letters = string.ascii_uppercase
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key


def encrypt(key, message):
    cypher = ""
    for c in message:
        if c in key:
            cypher += key[c]
        else:
            cypher += c
    return cypher


def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey


key = generate_key(3)
print(key)

message = "YOU ARE AWESOME"

cypher = encrypt(key, message)
print(cypher)

dkey = get_decryption_key(key)
print(dkey)

decryped_message = encrypt(dkey, cypher)
print(decryped_message)
