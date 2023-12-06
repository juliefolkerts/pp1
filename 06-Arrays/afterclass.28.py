def compare(array1, array2):
    if array1 == array2:
        return True
    else: 
        return False
    
print(compare(["water","book","sky"],["water","book","sky"]))
print(compare([True,False],[True,False,True]))
print(compare([5,3,1],[5,3,1]))
print(compare([3,2,1],[3,2]))