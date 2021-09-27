#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
# pip3 install pycryptodome
from pathlib import Path
import signal
import sys
import os

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


sys.stdout = Unbuffered(sys.stdout)
sys.stderr = open('/dev/null','w')


_MENU = """--------------------------
1. Dang ky
2. Dang nhap
3. Flag
4. Logout"""

USERNAME = None
BIOGRAPHY  = None
ROLE = None
KEY = open(os.path.join(Path(__file__).parent.absolute(),'key'),'rb').read()
FLAG = open(os.path.join(Path(__file__).parent.absolute(),'flag'),'rb').read()


def is_ascii(s):
    return all((ord(c) < 128) and (ord(c) > 31) for c in s)

def encrypt_aes(plaintext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    pad_plaintext = pad(plaintext.encode('utf-8'),16)
    return cipher.encrypt(pad_plaintext)

def decrypt_aes(ciphertext):
    decipher = AES.new(KEY, AES.MODE_ECB)
    unpad_plaintext = decipher.decrypt(ciphertext)
    return unpad(unpad_plaintext,16)

def register():
    global USERNAME,BIOGRAPHY,ROLE
    USERNAME = input('Ten dang nhap: ')
    BIOGRAPHY = input('So luoc ban than: ')
    ROLE = 0

    if not is_ascii(USERNAME) or not is_ascii(BIOGRAPHY):
        print(bcolors.WARNING + 'Du lieu chi duoc chua cac ki tu ASCII >_<' + bcolors.ENDC)
        USERNAME = None
        BIOGRAPHY = None
        ROLE = None

    if USERNAME and BIOGRAPHY:
        print(bcolors.OKGREEN + 'Ban da dang ky thanh cong!' + bcolors.ENDC)

def info():
    global USERNAME,BIOGRAPHY,ROLE
    print(bcolors.OKBLUE+"[+] Ten dang nhap: {}\n[+] So luoc ban than: {}\n[+] Quyen han: {}".format(USERNAME,BIOGRAPHY,ROLE))
    if ROLE == 0:
        print('Hm...ban khong phai admin!')
    elif ROLE == 1:
        print('Xin chao admin!')
        print('Day la flag cua ban: {}'.format(FLAG))
    print(bcolors.ENDC)

def parse(info):
    global USERNAME,BIOGRAPHY,ROLE
    block = info.split('\x00')
    print('[PARSING DEBUG]',block)
    try:
        for b in block:
            if b.startswith('USERNAME='):
                USERNAME = b[9:]
            if b.startswith('BIOGRAPHY='):
                BIOGRAPHY = b[10:]
            if b.startswith('ROLE='):
                ROLE = int(b[5:])

        if USERNAME != None and BIOGRAPHY != None and ROLE != None:
            return True
        else:
            return False
    except:
        return False


def login():
    global USERNAME,BIOGRAPHY,ROLE
    cre = input('Hay dien cookie dang nhap cua ban: ')
    plaintext = decrypt_aes(bytes.fromhex(cre)).decode('utf-8')
    if parse(plaintext):
        print(bcolors.OKGREEN+'Ban da dang nhap thanh cong!\nXin chao {} ^_^'.format(USERNAME) + bcolors.ENDC)
    else:
        USERNAME = None
        BIOGRAPHY = None
        ROLE = None
        print(bcolors.FAIL + 'Cookie dang nhap cua ban khong hop le >_<' + bcolors.ENDC)



def gen_credential():
    cre = "USERNAME={}\x00BIOGRAPHY={}\x00ROLE={}".format(USERNAME,BIOGRAPHY,ROLE)
    cre = encrypt_aes(cre)
    return cre.hex()

print(bcolors.FAIL + "< WIBU FANCLUB SYSTEM >" + bcolors.ENDC)

while True:
    print(_MENU)
    choice = input(">>> ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        info()
    else:
        break

if USERNAME != None:
    print('Day la cookie dang nhap cua ban, hay su dung no o lan ke tiep!')
    print(bcolors.OKGREEN+gen_credential()+bcolors.ENDC)
    print('~')

print('Bye!')
