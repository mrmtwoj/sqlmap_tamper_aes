#!/usr/bin/env python3

# pip install cryptography
# pip install crypto
# pip install Padding

# AES FROM
from Crypto.Cipher import AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import base64 

key = b"\xc3\x83\xf6\xdb\xdf{\xc5\xe8\x00\xe5u'\x9e{o\x19" #Must Be 16 char for AES128
iv =  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' #16 char for AES128


def dependencies():
    pass

def encrypt(data,key,iv):
        data= pad(data.encode(),16) # Fix Error Binary Sqlmap
        cipher = AES.new(key,AES.MODE_CBC,iv)
        return (cipher.encrypt(data))

def tamper(payload, **kwargs):
    return base64.b64encode(encrypt(payload,key,iv)).decode('utf-8')
    # Fix Error object C in sqlmap .decode('utf-8')