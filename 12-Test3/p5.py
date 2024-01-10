class C():
    def __init__(self,number):
        self.number = number
    
    def m1(self):
        print(int(self.number))
    
    def m2(self):
        self.number +=1

    def m3(self):
        self.number -= 1

    def m4(self,n):
        self.n = n
        self.number += int(n)

    def __str__(self):
        print(str(self.number))
    

if __name__=='__main__':
    c=C(5)
    c.m1()
    c.m2()
    c.m1()
    c.m4(-8)
    c.m1()
    c.m3()
    c.m1()
    c.m4(10)
    c.m1()
    c.__str__()