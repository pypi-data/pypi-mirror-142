from .myHttp import *
from .others import *
import time
import json
import base64
import hmac

def _okexBasic_getFormatTime():
    t=time.gmtime()[0:6]
    ft=str(t[0])+'-'
    if(t[1]<=9):
        ft=ft+'0'
    ft=ft+str(t[1])+'-'
    if(t[2]<=9):
        ft=ft+'0'
    ft=ft+str(t[2])+'T'
    if(t[3]<=9):
        ft=ft+'0'
    ft=ft+str(t[3])+':'
    if(t[4]<=9):
        ft=ft+'0'
    ft=ft+str(t[4])+':'
    if(t[5]<=9):
        ft=ft+'0'
    ft=ft+str(t[5])
    ft=ft+'.'+str(getTime()%1000)+'Z'
    return ft

def _okexBasic_sha256(Text:str,Key:str): # 已验证没有问题
    sign=hmac.new(Key.encode('utf-8'),Text.encode('utf-8'),digestmod='sha256').digest()
    sign=base64.b64encode(sign)
    sign=str(sign,'utf-8')
    return sign




def okGet(BasicUrl:str,Parameters:dict,TimeOut:int=0): # 这是不需要签名的
    timeOut=TimeOut
    while(BasicUrl.find('<')>=0):
        n1=BasicUrl.find('<')
        n2=BasicUrl.find('>')
        name=BasicUrl[n1+1:n2]
        value=str(Parameters[name])
        Parameters.pop(name)
        BasicUrl=BasicUrl[0:n1]+value+BasicUrl[n2+1:]
    url=BasicUrl
    if(len(Parameters)!=0):
        url=url+'?'
        for k,v in Parameters.items():
            url=url+str(k)+'='+str(v)+'&'
        url=url[:-1]
    r=http(url,Timeout=timeOut)
    return r

def okSign(BasicUrl:str,APIList:list,Parameters:dict,TimeOut:int=0,isSimlated:bool=False):
    # GET  APIList=[APIKey,SecretKey,PassPhrase]
    header={}
    t=_okexBasic_getFormatTime()
    header['Content-Type']='application/json'
    header['OK-ACCESS-KEY']=APIList[0]
    header['OK-ACCESS-PASSPHRASE']=APIList[2]
    header['OK-ACCESS-TIMESTAMP']=t
    if(isSimlated):
        header['x-simulated-trading']=1
    while(BasicUrl.find('<')>=0):
        n1=BasicUrl.find('<')
        n2=BasicUrl.find('>')
        name=BasicUrl[n1+1:n2]
        value=str(Parameters[name])
        Parameters.pop(name)
        BasicUrl=BasicUrl[0:n1]+value+BasicUrl[n2+1:]
    url=BasicUrl
    if(len(Parameters)!=0):
        url=url+'?'
        for k,v in Parameters.items():
            url=url+str(k)+'='+str(v)+'&'
        url=url[:-1]
    n=url.find('/',5+url.find('://'))
    sigUrl=url[n:]
    sigStr=t+'GET'+sigUrl
    sig=_okexBasic_sha256(sigStr,APIList[1])
    header['OK-ACCESS-SIGN']=sig
    r=http(url,Header=header,Timeout=TimeOut)
    return r


def okPost(BasicUrl:str,APIList:list,Parameters:dict,TimeOut:int=0,isSimlated:bool=False):
    header={}
    t=_okexBasic_getFormatTime()
    header['Content-Type']='application/json'
    header['OK-ACCESS-KEY']=APIList[0]
    header['OK-ACCESS-PASSPHRASE']=APIList[2]
    header['OK-ACCESS-TIMESTAMP']=t
    if(isSimlated):
        header['x-simulated-trading']=1
    while(BasicUrl.find('<')>=0):
        n1=BasicUrl.find('<')
        n2=BasicUrl.find('>')
        name=BasicUrl[n1+1:n2]
        value=str(Parameters[name])
        Parameters.pop(name)
        BasicUrl=BasicUrl[0:n1]+value+BasicUrl[n2+1:]
    body=json.dumps(Parameters)
    url=BasicUrl
    n=url.find('/',5+url.find('://'))
    sigUrl=url[n:]
    sigStr=t+'POST'+sigUrl+body
    sig=_okexBasic_sha256(sigStr,APIList[1])
    header['OK-ACCESS-SIGN']=sig
    r=http(url,Method='POST',Header=header,Timeout=TimeOut,BODY=body)
    return r


