class C():
    def __init__(self,dic):
        self.dic = dic

    def m1(self,s,n):
        self.dic[s] = n

    def m2(self,s):
        sum = 0
        for i in range(0,len(s)):
            sum += int(self.dic[(s[i])])
        return sum
    
c1 = C({"A":120,"D":150,"G":90,"K":110})
c1.m1("G",130)
print(c1.m2("GD"))
print(c1.m2("KEJ"))
