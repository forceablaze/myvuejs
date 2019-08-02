import parse
import re

from django.conf import settings

def getSymbolValue(tag, symbolName):
    symbols = settings.SYMBOL_TABLE.getSymbolsByTag(tag)
    for sym_hash in symbols:
        symbol = symbols[sym_hash]
        if symbol.getSymbolShortName() == symbolName:
            return symbol.getSymbolConvertedValue()
    return None

# x_name is the key of param to compare, defined in cvlog/report.py
def isLogParamEqual(logObj, x_name, value):
    if x_name == 'logid':
        logid = parse.parse("0x{:x}", logObj[x_name])[0]
        if logid == value:
            return True

    elif re.match("^part\d+", x_name):
        index = parse.parse("part{:d}", x_name)[0] - 1
        if logObj['params'][index] == value:
            return True
    else:
        pass
    return False

def filterLogWithParam(logObj, x_name, value):
    return list(filter(lambda x: x[x_name] == value, logObj))

def filterPFTypeLog(logObj):
    return list(filter(lambda x: x['apitype'].isdigit(), logObj))

def isLogHasParams(log, params_items):

    # param_name is the symbol tag name
    # obj['name'] is the symbol short name
    for param_name, obj in params_items.items():

        if obj is None:
            continue

        value = getSymbolValue(param_name, obj['name'])
        if value is not None:
            if not isLogParamEqual(log, obj['dest'], value):
                return False
            '''
            else:
                print('log {} match'.format(log['index']))
            '''
        else:
            return False

    return True
