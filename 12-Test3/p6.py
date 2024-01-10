def f(vname):
    count = 0
    vname = list(vname)
    if vname[0] != '_':
        vname[0] = vname[0].lower()
    if vname[0] == 'a' or vname[0] =='b' or vname[0] == 'c' or vname[0] == 'd' or vname[0] == 'e' or vname[0] =='f' or vname[0] =='g' or vname[0] =='h' or vname[0] =='i' or vname[0] =='j' or vname[0] =='k' or vname[0] =='l' or vname[0] =='m' or vname[0] =='n' or vname[0] =='o' or vname[0] =='p' or vname[0] =='q' or vname[0] =='r' or vname[0] =='s' or vname[0] =='t' or vname[0] =='u' or vname[0] =='v' or vname[0] =='w' or vname[0] =='x' or vname[0] =='y' or vname[0] =='z' or vname[0] == '_':
        count =0
        for i in range(1,len(vname)):
            if vname[i] == '_' or vname[i] == '1' or vname[i] == '2' or vname[i] == '3' or vname[i] == '4' or vname[i] == '5'or vname[i] == '6' or vname[i] == '7' or vname[i] == '8' or vname[i] == '9' or vname[i] == '0':
                count = count
            elif vname[0] == 'a' or vname[0] =='b' or vname[0] == 'c' or vname[0] == 'd' or vname[0] == 'e' or vname[0] =='f' or vname[0] =='g' or vname[0] =='h' or vname[0] =='i' or vname[0] =='j' or vname[0] =='k' or vname[0] =='l' or vname[0] =='m' or vname[0] =='n' or vname[0] =='o' or vname[0] =='p' or vname[0] =='q' or vname[0] =='r' or vname[0] =='s' or vname[0] =='t' or vname[0] =='u' or vname[0] =='v' or vname[0] =='w' or vname[0] =='x' or vname[0] =='y' or vname[0] =='z' or vname[0] == '_' or vname[0] == 'A' or vname[0] =='B' or vname[0] == 'C' or vname[0] == 'D' or vname[0] == 'E' or vname[0] =='F' or vname[0] =='G' or vname[0] =='H' or vname[0] =='I' or vname[0] =='J' or vname[0] =='K' or vname[0] =='L' or vname[0] =='M' or vname[0] =='N' or vname[0] =='O' or vname[0] =='P' or vname[0] =='Q' or vname[0] =='R' or vname[0] =='S' or vname[0] =='T' or vname[0] =='U' or vname[0] =='V' or vname[0] =='W' or vname[0] =='X' or vname[0] =='Y' or vname[0] =='Z':
                count = count
            else:
                count += 1
    else:
        count += 1
    if 5>=len(vname) > 1:
        count = count
    else:
        count += 1
    if count == 0:
        result = True
    else:
        result = False
    return result

if __name__=='__main__':
    print(f('abc'))
    print(f('Abc'))
    print(f('abcdef'))
    print(f('_ab_c'))
    print(f('8abc'))
