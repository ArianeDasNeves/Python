# Write a program that calculates the amount to be paid for a product, taking into account its regular price and payment terms:
# – Cash or check: 10% discount
# – Credit card (one-time payment): 5% discount
# – Credit card (up to 2 installments): full price
# – Credit card (3 or more installments): 20% interest
c = float(input('How much does the product cost? '))
p = str.strip(input('What is the payment method (cheque/cash/debit card/credit card)? '))
l = p.lower()
if l == 'cash' or l == 'cheque':
    print('You have 10% of discount')
    print('You will pay {:.2f}'.format(c*90/100))
if l == 'debit card':
    print('You have 5% of discount')
    print('You will pay {:.2f}'.format(c * 95 / 100))
if l == 'credit card':
    t = int(input('How many times on the credit card?'))
    if t <= 2:
        print('You will pay the normal price')
    elif t > 3:
        print('You will pay {:.2f}'.format(c*120/100))
