while True:
    try:
        a10 = int(input('Целое число: '))
        system = int(input('Система счисления: '))
        break
    except(ValueError, TypeError):
        print('Введите другое значение')

a = ''

if system == 2:
    while a10 > 0:
        a = str(a10%2) + a
        a10 //= 2

if system == 8:
    while a10 > 0:
        a = str(a10%8) + a
        a10 //= 8

print(a)