from .myHttp import *
from .others import *
import time 
import hmac
import base64
import json
from urllib.parse import quote


def _huobiBasic_getFormatTime():
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
    ft=ft+str(t[3])+'%3A'
    if(t[4]<=9):
        ft=ft+'0'
    ft=ft+str(t[4])+'%3A'
    if(t[5]<=9):
        ft=ft+'0'
    ft=ft+str(t[5])
    return ft

def _huobiBasic_sha256(Text:str,Key:str): # 已验证没有问题
    sign=hmac.new(Key.encode('utf-8'),Text.encode('utf-8'),digestmod='sha256').digest()
    sign=base64.b64encode(sign)
    sign=str(sign,'utf-8')
    sign=quote(sign,'utf-8')
    return sign


def hbGet(BasicUrl:str,Parameters:dict,TimeOut:int=0): # 这是不需要签名的
    # 不需要签名，参数无顺序要求
    basicUrl=BasicUrl
    parameters=Parameters
    timeOut=TimeOut
    url=basicUrl
    if(len(parameters)!=0):
        url=url+'?'
        for k,v in parameters.items():
            url=url+str(k)+'='+str(v)+'&'
        url=url[:-1]
    r=http(url,Timeout=timeOut)
    return r


#def hbSign(BasicUrl:str,API_Key:str,SecretKey:str,Parameters:dict,TimeOut:int=0):
def hbSign(BasicUrl:str,APIList:list,Parameters:dict,TimeOut:int=0):
    # GET
    API_Key=APIList[0]
    SecretKey=APIList[1]
    if(BasicUrl.find('{')>=0):
        n1=BasicUrl.find('{')
        n2=BasicUrl.find('}')
        name=BasicUrl[n1+1:n2]
        value=str(Parameters[name])
        Parameters.pop(name)
        BasicUrl=BasicUrl[0:n1]+value+BasicUrl[n2+1:]
    Parameters['AccessKeyId']=API_Key
    Parameters['SignatureMethod']='HmacSHA256'
    Parameters['SignatureVersion']=2
    Parameters['Timestamp']=_huobiBasic_getFormatTime()
    paraList=[]
    for k,v in Parameters.items():
        paraList.append(str(k)+'='+str(v))
    paraList.sort()
    paraStr=''
    for i in range(0,len(paraList)):
        paraStr=paraStr+paraList[i]+'&'
    paraStr=paraStr[0:-1]
    n=BasicUrl.find('://')
    url=BasicUrl[n+3:]
    n=url.find('/')
    domain=url[0:n]
    aft=url[n:]
    sigStr="GET\n"+domain+'\n'+aft+'\n'+paraStr
    sig=_huobiBasic_sha256(sigStr,SecretKey)
    paraStr=paraStr+'&Signature='+sig
    url=BasicUrl+'?'+paraStr
    r=http(url,Timeout=TimeOut)
    return r

#def hbPost(BasicUrl:str,API_Key:str,SecretKey:str,Parameters:dict,TimeOut:int=0):
def hbPost(BasicUrl:str,APIList:list,Parameters:dict,TimeOut:int=0):
    API_Key=APIList[0]
    SecretKey=APIList[1]
    if(BasicUrl.find('{')>=0):
        n1=BasicUrl.find('{')
        n2=BasicUrl.find('}')
        name=BasicUrl[n1+1:n2]
        value=str(Parameters[name])
        Parameters.pop(name)
        BasicUrl=BasicUrl[0:n1]+value+BasicUrl[n2+1:]
    urlPara={}
    urlPara['AccessKeyId']=API_Key
    urlPara['SignatureMethod']='HmacSHA256'
    urlPara['SignatureVersion']=2
    urlPara['Timestamp']=_huobiBasic_getFormatTime()
    urlParaList=[]
    for k,v in urlPara.items():
        urlParaList.append(str(k)+'='+str(v))
    urlParaList.sort()
    urlParaStr=''
    for i in range(0,len(urlParaList)):
        urlParaStr=urlParaStr+urlParaList[i]+'&'
    urlParaStr=urlParaStr[0:-1]
    n=BasicUrl.find('://')
    url=BasicUrl[n+3:]
    n=url.find('/')
    domain=url[0:n]
    aft=url[n:]
    sigStr="POST\n"+domain+'\n'+aft+'\n'+urlParaStr
    sig=_huobiBasic_sha256(sigStr,SecretKey)
    urlParaStr=urlParaStr+'&Signature='+sig
    url=BasicUrl+'?'+urlParaStr
    paraStr=json.dumps(Parameters)
    header={'Content-Type':'application/json'}
    r=http(url,Method='POST',Timeout=TimeOut,BODY=paraStr,Header=header)
    return r

