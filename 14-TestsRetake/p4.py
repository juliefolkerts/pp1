import re

def f(vname):
    result = False
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    if bool(pattern.match(vname)) == True:
        if 1<=len(vname) <=5:
            result = True
    return result

if __name__ == '__main__':
    print(f('8abc'))