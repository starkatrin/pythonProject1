def num_of_day():
    week = [1, 2, 3, 4, 5, 6, 7]
    try:
        number = int(input('Введите цифру, соответствующую дню недели:'))
        if number in week:
            if 1 <= number <= 5:
                answer = 'Нет'
            else:
                answer = 'Да'
            return answer
        else:
            print('Введите цифру от 1 до 7:')
            return num_of_day()
    except:
        print('Введите целое число от 1 до 7!')
        return num_of_day()

print(num_of_day())