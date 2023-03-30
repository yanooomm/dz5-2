'''
Напишите программу, которая заданное вещественное чсило выводит в формате с плавающей точкой в
нормализованной форме. Например:
Введите число: 0.0012
Формат плавающей точки: х=0.12*10**-2
'''

number = (input('Введите число: '))
if float(number) > 1.0:
    num = number.replace('.', '', 1)
    a = int(float(number))
    print('Формат с плавающей точкой: 0.' + str(num) + ' * 10 ** ' + str(len(str(a))))
elif float(number) < 1.0:
    num = number.strip('0.')
    ZeroCounter = number.strip(num)
    zero = len(ZeroCounter) - 1
    print('Формат с плавающей точкой: 0.' + num + ' * 10 ** -' + str(zero-1))

'''
Введите число: 0.000012
Формат с плавающей точкой: 0.12 * 10 ** -4
'''

'''
Введите число: 43.542
Формат с плавающей точкой: 0.43542 * 10 ** 2
'''
