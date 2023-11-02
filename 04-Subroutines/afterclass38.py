def f(palindrome):
    for i in range(0, len(palindrome)):
        if palindrome[i] == palindrome[-i-1]: #why -i-1 and not just -i?
            return True
        else:
            return False
        
result = f('radar')
print(result)