"""task_1"""


def input_log_and_password():
    m = 6
    while m > 3:
        login = input("Введите логин - ")
        password = int(input("Введите пароль - "))
        if login != "log" and password != 123456:
            m = m - 1
            print("")
            print("Повторите попытку.")
        else:
            exit("Логин и пароль совпадают!")
    exit("Система заблокирована. Повторите попытку через 5 минут!!!")


input_log_and_password()

# from time import time, sleep
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'RUN {func.__name__}; args {args}; kwargs {kwargs}')
#         start_time = time()
#         print(f'{start_time}')
#         result = func(*args, **kwargs)
#         print(f'Выполнено {func.__name__}')
#         end_time = time() - start_time
#         print(f'Время окончания {end_time}')
#         print(f'Всего затрачено времени Х{end_time - start_time}')
#         return result
#     return wrapper
#
#
# def class_decor(cls):
#     call_attr = {k: v for k, v in cls.__dict__.items() if callable(v)}
#
#     for name, func in call_attr.items():
#         dec_func = decorator(func)
#         setattr(cls, name, dec_func)
#     return cls

"""task_2"""


def get_info_author():
    full_name = input("Введите И.О.Фамилию - ")
    date_of_birth = input("Введите дату рождения - ")
    date_of_death = input("Введите дату смерти - ")
    info_author = input("Введите краткую информацию - ")
    print(f"{full_name}({date_of_birth} - {date_of_death}) - {info_author}")


get_info_author()

"""task_3"""


def two_three_digit(*args):
    two_digit = 0
    three_digit = 0
    for i in list(args):
        if len(str(i)) == 2:
            two_digit += 1
        elif len(str(i)) == 3:
            three_digit += 1
    return print(f"Количество двухзначных чисел - {two_digit}; \n"
                 f"Количество трехзначных чисел - {three_digit}.")


def determine_the_bit(*args):
    for index, elem in enumerate(args):
        print("")
        print(f"Число - {elem}")
        i = 0
        while elem > 0:
            elem = elem // 10
            i += 1
        print(f"Разрядность - {i}")


x = 55
y = 22
z = 123
q = 12354
w = 12544444
s = 155


two_three_digit(x, y, z, q, w, s)
determine_the_bit(x, y, z, q, w, s)
