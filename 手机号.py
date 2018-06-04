
import requests
import re
import time

def get_it(postid):
    url = 'http://www.kuaidi100.com/query'
    data = {"type": "youzhengguonei",
            "postid": postid,
            "id": "1"
            }
    r = requests.get(url, data)
    regx = re.compile('(.*)1\d{10}')
    regy = re.compile('1\d{10}')
    if regy.findall(r.text) and regx.findall(r.text):
        phone = regy.findall(r.text)[0]
        name = (regx.findall(r.text)[0])[-4:]
        s = '：'
        if s in name:
            name = name[-3:]
        return phone, name
    else:
        return





if __name__ == '__main__':
    postider = 9891000000000
    while True:
        a = get_it(str(postider))
        print(a)
        postider += 1
        time.sleep(3)

