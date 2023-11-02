def f(palindrome):
    for i in range(0, len(palindrome)):
        if palindrome[i] == palindrome[-i-1]:
            return True
        else:
            return False
        
result = f('radar')
print(result)