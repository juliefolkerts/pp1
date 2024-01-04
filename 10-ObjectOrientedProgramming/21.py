class Stat():
    def __init__(self,numbers=[]):
        self.numbers = numbers
    
    def add(self,nr):
        self.nr = int(nr)
        x = self.numbers
        x.append(self.nr)

    def display(self):
        return ' '.join(map(str, self.numbers))
        
    def biggest(self):
        self.biggestt = max(self.numbers)
        return max(self.numbers)
    
    def smallest(self):
        self.smallestt = min(self.numbers)
        return min(self.numbers)
    
    def mean(self):
        self.meann = (sum(self.numbers) / len(self.numbers))
        return (sum(self.numbers) / len(self.numbers))
    
    def median(self):
        self.numbers = sorted(self.numbers)
        if len(self.numbers) % 2 != 0:
            i = int(len(self.numbers)/2)
            self.mediann = self.numbers[i]
        else:
            i = (len(self.numbers)/2)
            self.mediann = (self.numbers[i-1]+self.numbers[i])/2


    def displaystats(self):
        return f'max: {self.biggestt}\nmin: {self.smallestt}\nmean: {self.meann}\nmedian: {self.mediann}'
    
stat1 = Stat()
stat1.add(12)
stat1.add(37)
stat1.add(6)
print(stat1.display())
stat1.biggest()
stat1.smallest()
stat1.mean()
stat1.median()
print(stat1.displaystats())
