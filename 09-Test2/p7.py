import re

def f(arr):
    count = 0
    for password in arr:
        if 12>= len(password) >= 4:
            x = re.findall(fr'[a-z0-9_]', password)
            if len(x) == len(password):
                count+= 1
    return count

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))