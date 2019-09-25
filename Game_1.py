print(" Игра угадай число")
from random import randint
x = randint(1,100)
z = False
while z == False:
    y = int(input('Выведите число от 1 до 100 = '))
    if y > x:
        print('Выведите маленькое число')
    elif y < x:
        print('Выведите большое число')
    else:
        z = True
        print('Поздравляем; Вы нашли его' )