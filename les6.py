# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

number = int(input('Введите количество чисел: ')) 

def sequence(number):

    return[round((1 + 1 / x)**x, 2) for x in range (1, number + 1)]   
        
print(sequence(number))
print(round(sum(sequence(number))))