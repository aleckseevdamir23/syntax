# *** Циклы ***

# Оператор while

# Бесконечный цикл
#while True:
#    print("Hello!")

# Цикл с условием
val_1 = 0 

#while val_1 <= 10:
#    print(f"Значение: {val_1}")
    # Инкремент
    #val_1 = val_1 + 1
#    val_1 += 1 

# Прерывание цикла по дополнительному условию

#while True:
#    val =input("Введите имя: ")
#    if val == "СТОП":
#        print("Bye-bye!")
#       break
#    print(f"Привет, {val}!")

# Пропуск части кода целиком

#val_1 = 0

#while val_1 < 20:
#    print(val_1)
#    val_1+= 1 

#    if val_1 < 10:
#        continue


    # 2 кусок кода
#    print("Hello")


# Оператор for

# 1. "Чтение" значения из обьектов с последовательностью по порядку
# 2. Считанное значение присваивает в собственную переменную
# 3. Выполняет код тела

lst_0 = [10, 20, 4, 3, 100, 234]

#for v in lst_0:
#    v *= 10
#    print(v)

dict_0 = dict(a=100, b=200, c=300)

#print(dict_0)

#for item in dict_0.items():
#    print(item)

#for k, v in dict_0.items():
#    print(k, v)

#val_1, val_2, val_3 = (100, 200, 300)

#print(val_1, val_2)

#for k in dict_0.values():
#    print(k)

# Класс range()

r = range(-10, 10, 2)

#print(r)

tuple_0 = tuple(r)

#print(tuple_0)

#for v in r:
#    print(v)

for v in range(5):
    v += 10
    print(v)
