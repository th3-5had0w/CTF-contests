import pycurl
from io import BytesIO
from bs4 import BeautifulSoup


'''
def crawlboi(url):
    b_obj = BytesIO()
    crl = pycurl.Curl()
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.setopt(crl.URL, url)
    crl.perform()
    dat = b_obj.getvalue()
    parsed = BeautifulSoup(dat, features="html.parser")
    print(url)
    for i in range(5):
        classiter = 'a-'+str(i)
        try:
            dir0 = parsed.body.find('div', attrs={'class':classiter}).text
            crawlboi(url+'/'+dir0)
        except:
            if (b'flag.txt' in dat):
                print(url)
                exit(0)
    return 0


url = 'http://178.128.19.56:17789'
dirs0 = ['bak', 'cgi', 'log', 'srv', 'var']

for k in dirs0:
    crawlboi(url+'/'+k)

b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.WRITEDATA, b_obj)
req = 'http://178.128.19.56:17789/bak/bak/bak/app'
crl.setopt(crl.URL, req)
crl.perform()
get_body = b_obj.getvalue()
parsed = BeautifulSoup(get_body, features="html.parser")
try:
    print(parsed.body.find('div', attrs={'class':'a-1'}).text)
except:
    if (b'flag.txt' in get_body):
        print(req)
        exit(0)


'''
#dirs1bak = ['bak', 'cgi', 'db', 'log', 'srv', 'app', 'cache', 'bin']

dirshac = ['/bak', '/cgi', '/log', '/srv', '/var', '/db', '/cache', '/conf', '/app', '/bin']


dirs = []
dirs.append('http://178.128.19.56:17789/bak/bak')
dirs.append('http://178.128.19.56:17789/bak/cgi')
dirs.append('http://178.128.19.56:17789/bak/db')
dirs.append('http://178.128.19.56:17789/bak/log')
dirs.append('http://178.128.19.56:17789/bak/srv')
dirs.append('http://178.128.19.56:17789/cgi/app')
dirs.append('http://178.128.19.56:17789/cgi/bak')
dirs.append('http://178.128.19.56:17789/cgi/cache')
dirs.append('http://178.128.19.56:17789/cgi/db')
dirs.append('http://178.128.19.56:17789/cgi/srv')
dirs.append('http://178.128.19.56:17789/log/bin')
dirs.append('http://178.128.19.56:17789/log/cgi')
dirs.append('http://178.128.19.56:17789/log/conf')
dirs.append('http://178.128.19.56:17789/log/log')
dirs.append('http://178.128.19.56:17789/log/var')
dirs.append('http://178.128.19.56:17789/srv/bin')
dirs.append('http://178.128.19.56:17789/srv/conf')
dirs.append('http://178.128.19.56:17789/srv/log')
dirs.append('http://178.128.19.56:17789/srv/src')
dirs.append('http://178.128.19.56:17789/srv/var')
dirs.append('http://178.128.19.56:17789/var/app')
dirs.append('http://178.128.19.56:17789/var/bak')
dirs.append('http://178.128.19.56:17789/var/cache')
dirs.append('http://178.128.19.56:17789/var/db')
dirs.append('http://178.128.19.56:17789/var/srv')


b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.WRITEDATA, b_obj)


for i in dirs:
    for j in dirshac:
        for k in dirshac:
            req = i + j + k
            print('Checking '+req)
            crl.setopt(crl.URL, req)
            crl.perform()
            get_body = b_obj.getvalue()
            if (b'flag.txt' in get_body) or (b'CTF{' in get_body):
                print('Correct: '+req)
                break
