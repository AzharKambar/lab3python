#является ли строка палиндромом
word = input("Введите слово: ")
if word == word[::-1]:
   print("Да , это палиндром")
else:
   print("Нет, это не палиндром")