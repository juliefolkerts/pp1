import re

def f(arr):
    count = 0
    for i in range(len(arr)):
        content = arr[i]
        if 12>=len(arr[i]) >=4:
            patern = re.compile(r'[a-z0-9_]')
            arra = re.findall(patern, content)
            if len(arra) == len(content):
                count+=1
    return count
            


print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
