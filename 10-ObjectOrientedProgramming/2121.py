class Stats():
    def __init__(self,arr=[]):
        self.arr = arr

    def new_nr(self,number):
        self.number = number
        self.arr.append(self.number)

    def display(self):
        return ' '.join(map(str, self.arr))

    def biggest(self):
        result = max(self.arr)
        return result

    def smallest(self):
        result = min(self.arr)
        return result
    
    def mean(self):
        result = sum(self.arr)/len(self.arr)
        return result

    def median(self):
        self.arr = sorted(self.arr)
        if len(self.arr)%2 != 0:
            i = int(len(self.arr)/2)
            result = self.arr[i]
        else:
            i = len(self.arr)/2
            result = (self.arr[i] + self.arr[i-1])/2
        return result
    
    def displayy(self):
        return f'maximum:{self.biggest()}\nminimum:{self.smallest()}\nmean:{self.mean()}\nmedian:{self.median()}'
         

numbers = Stats([12,37,6,9])
numbers.new_nr(17)
numbers.biggest()
numbers.smallest()
numbers.mean()
numbers.median()
print(numbers.display())
print(numbers.displayy())