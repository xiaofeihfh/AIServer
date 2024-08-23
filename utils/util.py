import base64

from Crypto.Cipher import AES

from AiServer.settings import AES_SECRET_KEY, AES_IV


def encrypt(data):
    cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
    padded_data = data + (16 - len(data) % 16) * ' '
    encrypted_data = cipher.encrypt(padded_data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')


def decrypt(encrypted_data):
    cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
    decoded_data = base64.b64decode(encrypted_data)
    decrypted_data = cipher.decrypt(decoded_data).decode('utf-8').strip()
    return decrypted_data
