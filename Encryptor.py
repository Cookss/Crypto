from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time

class Encryp:
    def __init__(self, key):
        self.key=key

    def pad(self,s):
        return s+b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size = 256):
        message = self.pad(message)
        ARandomThingLol = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, ARandomThingLol)
        return ARandomThingLol + cipher.encrypt(message)

    def FileEncryptor(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
            encry = self.encrypt(plaintext, self.key)
            with open(file_name + ".enc",'wb') as fo:
                fo.write(encry)
            os.remove(file_name)

    def Decryptor(self,cipherText, key):
        ARandomThingLol = cipherText[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, ARandomThingLol)
        plaintext = cipher.decrypt(cipherText[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def FileDecryptor(self, file_name):
        with open(file_name, 'rb') as fo:
            cipherText = fo.read()
        dec = self.Decryptor(cipherText, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def useAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if(fname != 'Untilted-2.py' and fname!='data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encryptAllFiles(self):
        dirs = self.useAllFiles()
        for file_name in dirs:
            self.FileEncryptor(file_name)

    def decryptAllFiles(self):
        dirs = self.useAllFiles()
        for file_name in dirs:
            self.FileDecryptor(file_name)

key = b'[EX\xc8\xd5\xbfi{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryp(key)
clear = lambda:os.system('cls')

if os.path.isfile('data.txt.enc'):
    while True:
        password = str(input("Enter password: "))
        enc.FileDecryptor("data.txt.enc")
        p = ""
        with open("data.txt") as f:
            p = f.readlines()
        if p[0]==password:
            enc.FileEncryptor("data.txt")
            break

    while True:
        clear()
        Answer = int(input('1 encrypt file. 2 decrypt file. 3 encrypt all files. 4 decrypt all files. 5 exit'))
        clear()
        if Answer == 1:
            enc.FileEncryptor(str(input("Enter file name (Encryption): ")))
        elif Answer == 2:
            enc.FileDecryptor(str(input("Enter file name (Decrypt): ")))
        elif Answer == 3:
            enc.encryptAllFiles()
        elif Answer == 4:
            enc.decryptAllFiles()
        elif Answer == 5:
            exit()
        else:
            print("no lol")
else:
    while True:
        clear()
        password = str(input("enter pass to access decryption: "))
        password2 = str(input("Retype pass: "))
        if password == password2:
            break
        else:
            print("Denied!")
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    enc.FileEncryptor("data.txt")
    print("Restart the program")
    time.sleep(15)
