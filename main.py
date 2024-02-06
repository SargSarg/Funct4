# a*x = b
# x = b/a
def linear_solve(a, b):
    return b/a
# 2*x = 9
print(linear_solve(2,9))


def koren_l(c, d):
    if c: # помним, что 0 интерпретируется как False, иначе — True
        return d/c
    elif not c and not d:  # снова используем числа в логических выражениях
        return "Бесконечное количество корней"
    else:
        return "Нет корней"
print(koren_l(4,9))


def D(a, b, c):
    return b ** 2 - 4 * a * c
def quadratic_solve(a,b,c):
    if D(a,b,c) < 0:
        return "Нет вещественных корней"
    elif D(a,b,c) == 0:
        return -b/(2*a)
    else:
        return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)
print(quadratic_solve(1, 2, 6))



M = {'a' : 1,
     'b' : 0,
     'c' : -1}
print(quadratic_solve(**M))

def min_list(L): #Рекурсивная функция находящая минимальный элемент списка
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

def mirror(a, res=0): #Рекурсивная ыункция зеркалящая числа но без нулей
    if a == 0:
        return res
    else:
        return mirror(a // 10, res * 10 + a % 10)


def equal(N, S): #Проверяет равна ли сумма цифр в числе N с просто числом S которая обязательно положительная
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)




iter_obj = iter("Hello!")
print(next(iter_obj))

#Декоратор
yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)
auth = yesno == "Y"
def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

@is_auth
def from_db():
 print("some data from database")

@is_auth
def change_profile():
 print("Profile has been changed")
from_db()



USERS = ['admin', 'guest', 'director', 'root', 'superstar']
yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)
auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")
def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещен")
    return wrapper
@is_auth
@has_access
def from_db():
    print("some data from database")
from_db()