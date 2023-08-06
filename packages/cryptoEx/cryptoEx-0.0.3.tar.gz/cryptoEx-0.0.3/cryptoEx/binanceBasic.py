from .myHttp import *
from .others import *

def bnGet(BasicUrl:str,Parameters:dict,API_Key:str='',TimeOut:int=0): # 这是不需要签名的
    basicUrl=BasicUrl
    parameters=Parameters
    APIKey=API_Key
    timeOut=TimeOut
    url=basicUrl
    if(len(parameters)!=0):
        url=url+'?'
        for k,v in parameters.items():
            url=url+str(k)+'='+str(v)+'&'
        url=url[:-1]
    header={}
    if(APIKey!=''):
        header={'X-MBX-APIKEY':APIKey}
    r=http(url,Header=header,Timeout=timeOut)
    return r

def bnSign(BasicUrl:str,API_Key:str,SecretKey:str,Parameters:dict,TimeOut:int=0):
    # GET 且需要签名的
    header={'X-MBX-APIKEY':API_Key}
    body=''
    for k,v in Parameters.items():
        body=body+str(k)+'='+str(v)+'&'
    body=body+'timestamp='+str(getTime())
    sig=sha256(body,SecretKey)
    body=body+'&signature='+sig
    url=BasicUrl+'?'+body
    r=http(url,Header=header,Timeout=TimeOut)
    return r

def bnPPD(BasicUrl:str,API_Key:str,SecretKey:str,Parameters:dict,Method:str='POST',TimeOut:int=0):
    # PPD: POST, PUT, DELETE
    m=Method
    body=''
    for k,v in Parameters.items():
        body=body+str(k)+'='+str(v)+'&'
    body=body+'timestamp='+str(getTime())
    sig=sha256(body,SecretKey)
    body=body+'&signature='+sig
    header={'X-MBX-APIKEY':API_Key,'Content-Type':'application/x-www-form-urlencoded'}
    r=http(BasicUrl,Header=header,Timeout=TimeOut,BODY=body,Method=m)
    return r

