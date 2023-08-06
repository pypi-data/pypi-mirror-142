
import requests
import rsa
import base64
from bs4 import BeautifulSoup


def encryptPass(password):
    key_str = '''-----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDl/aCgRl9f/4ON9MewoVnV58OL
    OU2ALBi2FKc5yIsfSpivKxe7A6FitJjHva3WpM7gvVOinMehp6if2UNIkbaN+plW
    f5IwqEVxsNZpeixc4GsbY9dXEk3WtRjwGSyDLySzEESH/kpJVoxO7ijRYqU+2oSR
    wTBNePOk1H+LRQokgQIDAQAB
    -----END PUBLIC KEY-----'''
    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.encode('utf-8'))
    crypto = base64.b64encode(rsa.encrypt(
        password.encode('utf-8'), pub_key)).decode()
    return crypto



def login(username,password):
    # try:
    if True:
        url1 = 'https://oauth.shu.edu.cn/login/eyJ0aW1lc3RhbXAiOjE2NDY3NTE1MjUwOTA3NjYxMDksInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IlAzV25LVW5lQk1EUndza05lTzh3Z283YiIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cDovL3NodS5meXNzby5jaGFveGluZy5jb20vc3NvL3NodSIsInN0YXRlIjoiIn0='
        sess = requests.session()
        header = {
            'authority': 'oauth.shu.edu.cn',
            'method': 'POST',
            'path': '/login/eyJ0aW1lc3RhbXAiOjE2NDY3NTIyNzUxMjA3NDA0MzksInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IlAzV25LVW5lQk1EUndza05lTzh3Z283YiIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cDovL3NodS5meXNzby5jaGFveGluZy5jb20vc3NvL3NodSIsInN0YXRlIjoiIn0=',
            'scheme': 'https',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
            'origin': 'https://oauth.shu.edu.cn',
            'referer': 'https://oauth.shu.edu.cn/login/eyJ0aW1lc3RhbXAiOjE2NDY3NTIyNzUxMjA3NDA0MzksInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IlAzV25LVW5lQk1EUndza05lTzh3Z283YiIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cDovL3NodS5meXNzby5jaGFveGluZy5jb20vc3NvL3NodSIsInN0YXRlIjoiIn0='
        }
        res = sess.post(url1, data={
                        'username': username,
                        'password': encryptPass(password)
                        }, headers = header,allow_redirects=False)

        url2 = 'https://oauth.shu.edu.cn'+res.headers['Location']
        res = sess.get(url2, headers = header,allow_redirects=False)
        url3 = res.headers['Location']
        res = sess.get(url3, headers = header,allow_redirects=False)
        url4 = res.headers['Location']
        res = sess.get(url4, headers = header,allow_redirects=True).text

        soup = BeautifulSoup(res,'lxml')
        url5 = soup.select('form')[0].get('action')
        params = soup.select('input')
        pp = {}
        for i in params:
            if i['type'] == "hidden":
                newParam = {i['name']:i['value']}
                pp.update(newParam)
        res = sess.post(url5, params = pp,headers = header,allow_redirects=False)
        ###################################################################     登陆验证
        # print(res.cookies)
        cookie = requests.utils.dict_from_cookiejar(sess.cookies)
        res = sess.get('http://i.mooc.elearning.shu.edu.cn/space/index')
        soup = BeautifulSoup(res.text,'lxml')
        name = soup.find(class_ = 'personalName').get('title')
        print(name,'登陆成功')

        return name,cookie['UID'],sess
    # except:
    #     print('登陆失败')





