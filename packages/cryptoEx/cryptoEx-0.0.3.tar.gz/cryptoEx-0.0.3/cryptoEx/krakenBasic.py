from .myHttp import *
from .others import *
import urllib.parse as parse
import hashlib
import hmac
import base64




def _krakenBasic_get_kraken_signature(urlpath, data, secret):
    # 直接从 API 文档复制的
    postdata = parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    #print(message)
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

def _krakenBasic_isFuture(url:str):
    return url.find('futures.')>=0


def _krakenBasic_sign_message(endpoint, postData, SecretKey,nonce):
    if endpoint.startswith('/derivatives'):
        endpoint = endpoint[len('/derivatives'):]
    nonce=str(nonce)
    # step 1: concatenate postData, nonce + endpoint
    message = postData + nonce + endpoint
    # step 2: hash the result of step 1 with SHA256
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode('utf8'))
    hash_digest = sha256_hash.digest()
    # step 3: base64 decode apiPrivateKey
    secretDecoded = base64.b64decode(SecretKey)
    # step 4: use result of step 3 to has the result of step 2 with HMAC-SHA512
    hmac_digest = hmac.new(secretDecoded, hash_digest,
                           hashlib.sha512).digest()
    # step 5: base64 encode the result of step 4 and return
    return base64.b64encode(hmac_digest)



def kkGet(BasicUrl:str,Parameters:dict,TimeOut:int=0): # 不需要签名的
    while(BasicUrl.find('{')>=0):
        n1=BasicUrl.find('{')
        n2=BasicUrl.find('}')
        name=BasicUrl[n1+1:n2]
        value=str(Parameters[name])
        Parameters.pop(name)
        BasicUrl=BasicUrl[0:n1]+value+BasicUrl[n2+1:]
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


def kkPost(BasicUrl:str,APIList:list,Parameters:dict,TimeOut:int=0):
    if(_krakenBasic_isFuture(BasicUrl)):
        return _krakenBasic_futurePost(BasicUrl,APIList=APIList,Parameters=Parameters,TimeOut=TimeOut)
    header={}
    header['API-Key']=APIList[0]
    header['Content-Type']='application/x-www-form-urlencoded; charset=utf-8'
    Parameters['nonce']=getTime()
    n=BasicUrl.find('://')
    n=BasicUrl.find('/',n+5)
    urlpath=BasicUrl[n:]
    sig=_krakenBasic_get_kraken_signature(urlpath,Parameters,APIList[1])
    header['API-Sign']=sig
    body=''
    if(len(Parameters)!=0):
        for k,v in Parameters.items():
            body=body+str(k)+'='+str(v)+'&'
        body=body[0:-1]
    r=http(BasicUrl,Method='POST',Header=header,Timeout=TimeOut,BODY=body)
    return r


def kkSign(BasicUrl:str,APIList:list,Parameters:dict,TimeOut:int=0):
    # GET 且需要签名的
    header={}
    header["User-Agent"] = "cf-api-python/1.0"
    non=str(getTime())
    header['APIKey']=APIList[0]
    header['Nonce']=non
    n=BasicUrl.find('://')
    n=BasicUrl.find('/',n+5)
    urlpath=BasicUrl[n:]
    paraStr=''
    if(len(Parameters)!=0):
        for k,v in Parameters.items():
            paraStr=paraStr+str(k)+'='+str(v)+'&'
        paraStr=paraStr[0:-1]
    sig=_krakenBasic_sign_message(urlpath,paraStr,APIList[1],non)
    header['Authent']=sig
    url=BasicUrl
    if paraStr!='':
        url=BasicUrl+'?'+paraStr
    r=http(url,Header=header,Timeout=TimeOut)
    return r


def _krakenBasic_futurePost(BasicUrl:str,APIList:list,Parameters:dict,TimeOut:int=0):
    header={}
    header["User-Agent"] = "cf-api-python/1.0"
    non=str(getTime())
    header['APIKey']=APIList[0]
    header['Nonce']=non
    n=BasicUrl.find('://')
    n=BasicUrl.find('/',n+5)
    urlpath=BasicUrl[n:]
    paraStr=''
    if(len(Parameters)!=0):
        for k,v in Parameters.items():
            paraStr=paraStr+str(k)+'='+str(v)+'&'
        paraStr=paraStr[0:-1]
    sig=_krakenBasic_sign_message(urlpath,paraStr,APIList[1],non)
    header['Authent']=sig
    url=BasicUrl
    if paraStr!='':
        url=BasicUrl+'?'+paraStr
    r=http(url,Method='POST',Header=header,Timeout=TimeOut)
    return r

