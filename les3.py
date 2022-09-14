# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

number = int(input("Введите число: "))

def AmountSearch(number):
    if number >= 0:
        return sum([int(i) for i in str(number)])
    else:
        number = abs(number)
        Amount = sum([int(i) for i in str(number)])
        Amount -= int(str(number)[0]) * 2
        return Amount

def Arg(number):
    return [number] if number < 10 else Arg(number // 10) + [number % 10]
a = Arg(number)

if a == a[:: -1]:
    print("Это число палиндром")
else: 
    print("Это не палиндром, но к нему можно прийти: ")
    print (AmountSearch(number))

