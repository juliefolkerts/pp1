def a(txt):
    x = txt.split()
    return len(x)
txt ='An apple a day keeps the doctor away'
print(a(txt))

def b(txt):
    words = txt.split()
    n = len(words)
    for i in range(0,n):
        for j in range(0, n-i-1):
            if len(words[j]) < len(words[j+1]) :
                words[j], words[j+1] = words[j+1], words[j]
    return words

txt ='An apple a day keeps the doctor away'
print(b(txt))

def c(txt):
    x = txt.split()
    sorted_x = (sorted(x))
    return sorted_x

txt ='An apple a day keeps the doctor away'
print(c(txt)) 