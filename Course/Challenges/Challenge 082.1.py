#Create a program where the user enters any expression that uses parentheses. Your application should check whether the parentheses in the entered expression are opened and closed in the correct order.
n = str(input('Enter a expression: '))
l = []
for s in n:
    if s == '(':
        l.append(s)
    elif s == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(s)
            break
if len(l) == 0:
    print('Valid expression')
else:
    print('Invalid expression')
