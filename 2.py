def numbers_input():
    try:
        x, y, z = map(int, input('Введите числа x, y, z через пробел').split())
        return x, y, z
    except:
        print('Введите целое число!')
        return numbers_input()


def check_logik(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    if left == right is True:
        answer = 'Выражение истинно'
    else:
        answer = 'Выражение ложно'
    return answer


x, y, z = numbers_input()
print(check_logik(x, y, z))
