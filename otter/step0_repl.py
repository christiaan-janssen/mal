def READ(line: str) -> str:
    return line

def EVAL(line: str) -> str:
    return line

def PRINT(line: str) -> str:
    return line

def rep(line: str) -> str:
    re = READ(line)
    ev = EVAL(re)
    return PRINT(ev)

while(True):
    line = input('user> ')
    print(rep(line))
