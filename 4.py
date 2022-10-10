def numbers_input():
    try:
        a = float((input('Введите первое число:')))
        b = float((input('Введите второе число:')))
        operation = input('Введите знак операции над числами:')
        return a, b, operation
    except :
        print('Операции проводятся над числами')
        return numbers_input()


def calculate(a, b, operation):
    result = None
    try:
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '/':
            result = a / b
        elif operation == '*':
            result = a * b
        elif operation == 'mod':
            result = a % b
        elif operation == 'pow':
            result = a ** b
        elif operation == 'div':
            result = a // b
        else:
            print('Неизвестная операция')
        return result
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')



a, b, operation = numbers_input()
print(calculate(a, b, operation))