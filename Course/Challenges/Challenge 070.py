#Write a program that simulates the operation of an ATM. At the beginning, ask the user for the amount to be withdrawn (an integer), and the program will tell the user how many bills of each denomination will be dispensed. NOTE: Assume that the ATM has bills in denominations of R$50, R$20, R$10, and R$1.
v = int(input('How much are you going to withdraw from the cash machine? '))
c = t = d = u = 0
while True:
    resto = v % 50
    c = v // 50
    if resto > 0:
        t = resto // 20
        resto = resto % 20
        if resto > 0:
            d = resto // 10
            resto = resto % 10
            if resto > 0:
                u = resto // 1
                resto = resto % 1
                break
        else:
            break
    else:
        break
print(f'You are going withdraw \n({c}) 50 bills \n({t}) 20 bills \n({d}) 10 bills \n({u}) 1 bill')