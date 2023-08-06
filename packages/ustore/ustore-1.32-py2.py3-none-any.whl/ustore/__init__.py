import os
import platform
import hashlib
import json
import pyaes

__version__ = "1.0"
__author__ = 'JKinc'

udpath = ""

class Initialisation_Error(Exception):
    pass

class Invalid_Input_Error(Exception):
    pass

class User_Exists_Error(Exception):
    pass

class Invalid_Password_Error(Exception):
    pass

if platform.system() == "Windows":

    def init(userdatapath="."):
        global udpath
        udpath = userdatapath + "\\USERDATA\\"
        if not os.path.exists(udpath):
            os.mkdir(udpath)


    def register_account(user,password):

        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error

        passwordhash = hashlib.sha256(password.encode()).hexdigest()

        if os.path.exists(udpath + user + "\\"):
            raise User_Exists_Error

        os.mkdir(udpath + user + "\\")
        open(udpath + user + "\\password.ini","w").write(passwordhash)
    

    def setconfig(user,config,password):

        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error

        iv = "InitializationVe"
        if not hashlib.sha256(password.encode()).hexdigest() == open(udpath + user + "\\password.ini","r").read():
            raise Invalid_Password_Error

        key = hashlib.sha3_256(password.encode()).digest()
        aes = pyaes.AESModeOfOperationCTR(key)
        config = aes.encrypt(json.dumps(config))


        open(udpath + user + "\\config.ini","wb").write(config)


    def getconfig(user,password):

        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error


        iv = "InitializationVe"

        if not hashlib.sha256(password.encode()).hexdigest() == open(udpath + user + "\\password.ini","r").read():
            raise Invalid_Password_Error

        key = hashlib.sha3_256(password.encode()).digest()
        
        aes = pyaes.AESModeOfOperationCTR(key)
        config = json.loads(aes.decrypt(open(udpath + user + "\\config.ini","rb").read()))

        return config


    def valid_password(user,password):
        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error

        if not hashlib.sha256(password.encode()).hexdigest() == open(udpath + user + "\\password.ini","r").read():
            return False
        else:
            return True

else:

    def init(userdatapath="."):
        global udpath
        udpath = userdatapath + "/USERDATA/"
        if not os.path.exists(udpath):
            os.mkdir(udpath)


    def register_account(user,password):

        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error

        passwordhash = hashlib.sha256(password.encode()).hexdigest()

        if os.path.exists(udpath + user + "/"):
            raise User_Exists_Error

        os.mkdir(udpath + user + "/")
        open(udpath + user + "/password.ini","w").write(passwordhash)
    

    def setconfig(user,config,password):

        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error

        iv = "InitializationVe"
        if not hashlib.sha256(password.encode()).hexdigest() == open(udpath + user + "/password.ini","r").read():
            raise Invalid_Password_Error

        key = hashlib.sha3_256(password).digest()
        aes = pyaes.AESModeOfOperationCTR(key)
        config = aes.encrypt(json.dumps(config))


        open(udpath + user + "/config.ini","wb").write(config)


    def getconfig(user,password):

        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error


        iv = "InitializationVe"

        if not hashlib.sha256(password.encode()).hexdigest() == open(udpath + user + "/password.ini","r").read():
            raise Invalid_Password_Error

        key = hashlib.sha3_256(password).digest()
        
        aes = pyaes.AESModeOfOperationCTR(key)
        
        config = json.loads(aes.decrypt(open(udpath + user + "/config.ini","rb").read()))

        return config


    def valid_password(user,password):
        if not isinstance(user, str):
            raise Invalid_Input_Error
        if not isinstance(password, str):
            raise Invalid_Input_Error
        for i in user:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321-_":
                pass
            else:
                raise Invalid_Input_Error
        if udpath == "":
            raise Initialisation_Error

        if not hashlib.sha256(password.encode()).hexdigest() == open(udpath + user + "/password.ini","r").read():
            return False
        else:
            return True
