dict_dividers = [2]
for number in range(3, 200001):
    for divider in dict_dividers:
        while number % divider == 0:
            number = number // divider
    if number != 1:
        dict_dividers.append(number)
# print(dict_dividers)
dict_dividers_2 = [2]
for number in range(2, 200001):
    for divider in dict_dividers_2:
        if number % divider == 0:
            number = number // divider
    if number != 1:
        for divider_2 in dict_dividers:
            if divider_2 <= number:
                while number % divider_2 == 0:
                    dict_dividers_2.append(divider_2)
                    number = number // divider_2
            else:
                break
    
e = 1
for i in dict_dividers_2:
    e *= i
print(e)