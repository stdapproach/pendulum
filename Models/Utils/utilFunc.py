#utils function for function handling

# Get parameter by name from named parameters
def extractValue(name, **keywords):
    if name in keywords:
        val = keywords.get(name)
        #print('found key=',name,' val=', val)
        return val
    else:
        #print('NOT found key=',name)
        return None