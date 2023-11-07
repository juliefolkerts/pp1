def f(palindrome):
    for i in range(0, len(palindrome)):
        if palindrome[i] == palindrome[-i-1]: #why -i-1 and not just -i? #because the beginning starts with 0 but the end not if you go backwards
            return True
        else:
            return False
        
result = f('book')
print(result)