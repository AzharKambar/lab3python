#найти сумму цифр числа
num = input("Введите число: ")
sum = 0
#используем цикл for чтобы определить есть ли в строке цифры и вывести их сумму
for val in num:
    if val.isdigit():
        sum += int(val)
        print(f"Сумма цифр в данной строке : {sum}")

