total_zl = int(input('Enter amount of zloty:'))
#for total_zl // 5 == int:
print(f'5 zl-{int(total_zl // 5)}')
print(f'3 zl-{int((total_zl % 5) // 3)}')
print(f'2 zl-{int(int((total_zl % 5) // 3)) % 2}')