def READ(line):
    return line

def EVAL(line):
    return line 

def PRINT(line):
    return line

def rep(line):
    re = READ(line)
    ev = EVAL(re)
    return PRINT(ev)

while(True):
    line = input('user> ')
    print(rep(line))