a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = input('Введите действие: ')
if c == ':' or c == '/':
    print (f'{a} : {b} = ',a/b)
elif c == '*':
    print (f'{a} * {b} = ',a*b)
elif c == '+':
    print (f'{a} + {b} = ',a+b)
elif c == '-':
    print (f'{a} - {b} = ',a-b)
else:
    print('Неправильно введенное значение')
