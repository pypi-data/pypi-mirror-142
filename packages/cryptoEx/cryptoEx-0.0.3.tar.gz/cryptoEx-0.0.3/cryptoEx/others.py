import time
import json
import hmac

def getTime():
    t =time.time()
    t = int(1000 * t)
    return t


def toJson(Text):
    text=Text
    i=0
    while text[0]==' ' or text[0]=='\n':
        text=text[1:]
    if text[0]=='[':
        text='{"1":'+text+'}'
        i=1
    text=json.loads(text,strict=False)
    if i==1:
        text=text['1']
    return text

def sha256(Text:str,Key:str):
    sign=hmac.new(Key.encode('utf-8'),Text.encode('utf-8'),digestmod='sha256').hexdigest()
    return sign

