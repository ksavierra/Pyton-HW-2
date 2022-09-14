# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

print('Введите число: ')
n = int(input())
 
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
 
print(factorial)