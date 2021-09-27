#!/usr/bin/python3

import requests 
r = requests.session()

URL = "http://drive.kid.cyberjutsu-lab.tech/index.php"

def sendFile(pathToFile, fileName):
    content = open(pathToFile, 'rb')
    files = {'file': (fileName, content)}
    result = r.post(url= URL, files= files)
    print(result.text) # Mã nguồn HTML trả về

sendFile('test.txt', 'test.txt')