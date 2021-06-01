class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2 ** 31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

key = KeyStream(10)
print("key1 ",key)
message = "Hello World!".encode()
cipher = encrypt(key, message)
print(cipher)

key = KeyStream(10)
print("key2 ",key)
print(encrypt(key, cipher))
# for i in range(10):
#     print(key.get_key_byte())