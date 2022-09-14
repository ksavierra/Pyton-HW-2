# 1 - Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

number = int(input("Введите число: "))

def AmountSearch(number):
    if number >= 0:
        return sum([int(i) for i in str(number)])
    else:
        number = abs(number)
        Amount = sum([int(i) for i in str(number)])
        Amount -= int(str(number)[0]) * 2
        return Amount
print (AmountSearch(number))