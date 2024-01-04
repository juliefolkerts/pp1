from bankacc import Bankacc

bankacc1 = Bankacc('12 3456 5555 9090 1111 0000 7722')
print(bankacc1.display_info())
bankacc1.deposit(25.30)
print(bankacc1.display_info())
bankacc1.withdraw(31.70)
print(bankacc1.display_info())
bankacc1.withdraw(14.50)
print(bankacc1.display_info())
