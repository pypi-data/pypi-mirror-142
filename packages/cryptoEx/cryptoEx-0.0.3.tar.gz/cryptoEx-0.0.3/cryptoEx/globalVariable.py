from .DEVICE import DEVICE

_globalVar={} # 全局变量, 为避免过多及混乱, 全部储存在一个字典里
# 为保证安全, 在外部不可直接调用 globalVar, 必须通过函数调用
# 在外部调用 get 开头的函数时, 必须确保结果是只读的, 否则会对这里的可变对象的值产生影响

_globalVar['device']=DEVICE # 本地电脑为1, 服务器为0, 该值不可在函数中修改



def getGlobalValue(key):
    global _globalVar
    return _globalVar[key]


def setGlobalValue(key,v):
    global _globalVar
    _globalVar[key]=v


def getAllGlobalVariables():
    global _globalVar
    return _globalVar

def getGlobalVariableNum():
    global _globalVar
    return len(_globalVar)

def clearGlobalVariable():
    global _globalVar
    _globalVar={}

def deleteGlobalVariable(key):
    global _globalVar
    _globalVar.pop(key)


def getAllKeys():
    global _globalVar
    l=[]
    for k in _globalVar:
        l.append(k)
    return l

def isGlobalVariableExist(key):
    global _globalVar
    return key in _globalVar


def addGlobalVariable(key,num=1):
    global _globalVar
    try:
        _globalVar[key]=_globalVar[key]+num
    except:
        return -1
    return 0
