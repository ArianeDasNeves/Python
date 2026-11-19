#Create a program where the user enters any expression that uses parentheses. Your application should check whether the parentheses in the entered expression are opened and closed in the correct order.



n = str(input('Enter a numerical expression: '))
# c = 0
# a = 0
# while True:
#     if n.find('(') != -1:
#         if n.find(')') == -1:
#             print('The numeric expression is INVALID')
#             break
#         else:
#             a = 1
#     c += 1
#     if c == len(n):
#         break
# if a == 1:
#     print('The numeric expression is VALID')
# a = 0
# for c in range(0, len(n)):
#     if n[c] in '(':
#         a += 1
#     elif n[c] in ')':
#         a -= 1
#     if a < 0:
#         break
# print(n.count('('))
# print(n.count(')'))
# print(a)
# if a == 0:
#     print('The numeric expression is VALID')
# else:
#     print('The numeric expression is INVALID')
p = []
for s in n:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Valid expression')
else:
    print('Invalid expression')

