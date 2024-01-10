import re

def f(vname):
    result = False
    patter = re.compile(r'^[a-zA-Z_][aa-zA-Z0-9_]*$')
    if 1<=len(vname)<=5:
        if patter.match(vname):
            result = True
    return result

if __name__ == '__main__':
    print(f('_ab8_'))
