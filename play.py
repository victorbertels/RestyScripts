from math import prod


number1 = 20
number2 = 30

number3 = 40
number4 = 30

def multiplication_or_sum(num1, num2):
    product = num1*num2
    sum = num1 + num2
    if product <= 1000:
        return product
    else:
        return sum

print(multiplication_or_sum(20,30))
print(multiplication_or_sum(40,30))
