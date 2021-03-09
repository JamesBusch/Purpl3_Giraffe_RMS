'''
This file is too handle 
'''

from flask import jsonify
from cryptography.fernet import Fernet
import libpurpl3.preferences as pref 

#data[pref.getNoCheck(pref.LOGIN_USERNAME)]

#TODO add user sessions
def login(data: dict) -> str:
    #TODO get table to input static key
    currPassword = encryptPassword(data[pref.getNoCheck(pref.LOGIN_PASSWORD)], b'93fB_lc6JzlZQqh2ywiHCTyacWN1NQpCo3EORh_upiM=')
  
    return jsonify(
        Error = {
            "code":pref.Success.code,
            "str": str(pref.Success)
            },
        data = {
        "Success": True
        }
    )

def manageUser(data: dict) -> str:
    return jsonify(
        Error = {
            "code":pref.Success.code,
            "str": str(pref.Success)
            },
        data = {
        "Success": True
        }
    )

def changePassword(data: dict) -> str:
    return jsonify(
        Error = {
            "code":pref.Success.code,
            "str": str(pref.Success)
            },
        data = {
        "Success": True
        }
    )

def encryptPassword(password: str, key: str) -> str:
    '''
    This function takes in a given password and encryption key and returns
    the encrypted password.
    @param str password, the password for encrpytion
    @param str key, the encryption key
    @return a string of the ecrypted key
    '''
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(password.encode())

    return ciphered_text




