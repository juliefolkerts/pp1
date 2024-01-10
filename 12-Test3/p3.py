def f(uid):
    count = 0
    for i in range(0,len(uid)-1):
        for x in range(0,len(uid)):
            if i!=x:
                if uid[i] == uid[x]:
                    count +=1
                else:
                    count = count
    if count == 0:
        return True
    else:
        return False
    
if __name__=='__main__':
    print(f(['123','123','1','123']))
