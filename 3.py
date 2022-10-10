def numbers_input():
    try:
        x, y = map(float, input('Введите координаты точки x, y через пробел').split())
        return x, y
    except:
        print('Координаты должны быть числами!')
        return numbers_input()

def check_coord(x, y):
    if x > 0 and y > 0:
        res = '1 четверть'
    elif x > 0 and y < 0:
        res = '4 четверть'
    elif x > 0 and y == 0:
        res = 'ось х, положительная'
    elif x < 0 and y > 0:
        res = '2 четверть'
    elif x < 0 and y < 0:
        res = '3 четверть'
    elif x < 0 and y == 0:
        res = 'ось х, отрицательная'
    elif x == 0 and y > 0:
        res = 'ось y, положительная'
    elif x == 0 and y < 0:
        res = 'ось y, отрицательная'
    else:
        res = 'начало координат'
    return res


x, y = numbers_input()
print(check_coord(x, y))