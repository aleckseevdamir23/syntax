# Операции сравнения

x  = -3
y = 3

# "Операция меньше"
#  мы спрашиваем "значение x меньше значения y?"
res = x < y 

# "Операция меньше либо равно"  
#  мы спрашиваем "значение x меньше или равно значению y?"
res = x <= y

# "Операция больше"
#  мы спрашиваем "значение x больше значения y?"
res = x > y

# "Операция больше либо равно"
#  мы спрашиваем "значение x больше или равно значению y?"
res = x >= y 

#  Операция равенства (равно)
#  мы спрашиваем "значение x равно значению y?"
res = x == y

#  Операция НЕравенства (не равно)
#  мы спрашиваем "значение x НЕ равно значения y?"
res = x != y 

#print(res)


# Логические операции

v_1 = True
v_2 = False

# Оператор "НЕ" (NOT, инверция, отрицание)
res = not v_1

# Оператор "И" (AND, конъюнкция, логическое умножение)
# Возвращая True только тогда, когда оба значения True
res = v_1 and v_2

# Оператор "ИЛИ" (OR, дизъюнкция, логическое сложение)
# Возвращает False толькo тогда, когда оба значения False
res = v_1 or v_2

#print(res)

a = 3
b = 0

res = (a < 5) and not (b == 0) 

#print(res)


# Условные операции

a = 0

# Оператор "if" (если)
#if a == 0:
    #print("hello!")
    
# Оператор else (иначе)
b = 2

#if b < 20:
    #res = "меньше 20"
#else:
    #res = "больше либо равно 20"

# Оператор elif (else if)
a = -10

res = ""

if a > 0:
    res = "больше нуля"
elif a < 0: 
    res = "меньше нуля"
else:
    res = "равно нулю"

#print(res)


# Пример простого калькулятора

value_1 = int(input("Введите 1 число: "))
value_2 = int(input("Введите 2 число: "))

operator = input("Введите операцию: ")

if operator == '+':
    result = value_1 + value_2
elif operator == '-':
    result = value_1 - value_2
elif operator == '*':
    result = value_1 * value_2
elif operator == '/':
    result = value_1 / value_2
else:
    result = "Оператор не распознан!!!"

print(f"Результат = {result}")