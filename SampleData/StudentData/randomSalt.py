import os
import hashlib

def random_salt():
    return os.urandom(64)

def hash_password_and_salt(password: bytes, salt: bytes):
    return hashlib.pbkdf2_hmac('sha512', password, salt, 100_000).hex()