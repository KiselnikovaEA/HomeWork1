#weekDay = int(input('Введите номер дня недели: '))
#if weekDay == 6 or weekDay == 7:
#    print('День недели является выходным')
#else:
#    print('День недели не является выходным')



#for i in 0,1:
#    for j in 0,1:
#        for k in 0,1:
#            res = not (i or j or k) == (not i) and (not j) and (not k)
#            print(f'{i}{j}{k} = {res}')



#x = int(input('Введите координату х: '))
#y = int(input('Введите координату y: '))
#if x != 0 and y != 0:
#    if x > 0 and y > 0:
#        print('Точка находится в 1-й четверти')
#    elif x < 0 and y > 0:
#        print('Точка находится во 2-й четверти')
#    elif x < 0 and y < 0:
#        print('Точка находится в 3-й четверти')
#    elif x > 0 and y < 0:
#        print('Точка находится в 4-й четверти')
#else:
#    print('Координаты не должны быть равны нулю')



#x = int(input('Введите номер четверти: '))
#if x == 1:
#    print('x > 0, y > 0')
#elif x == 2:
#    print('x < 0, y > 0')
#elif x == 3:
#    print('x < 0, y < 0')
#elif x == 4:
#    print('x > 0, y < 0')
#else:
#    print('Существует только 4 четверти')


import math

x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))
AB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(AB)