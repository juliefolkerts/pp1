class C():
    def __init__(self,dic):
        self.dic = dic
    def m1(self,s,n):
        self.s = s
        self.n = n
        self.dic[s] = n

    def m2(self,s):
        self.s = s
        sum = 0
        for i in range(0,len(s)):
            if s[i] in self.dic:
                sum += int(self.dic[(s[i])])
            else:
                sum = sum
        result =  print(sum)
        return result
    
a = C({"A":120,"D":150,"G":90,"K":110})
a.m1("G",130)
a.m2("GD")
a.m2("KEJ")

