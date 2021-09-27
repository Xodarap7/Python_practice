################################################################################
# Посчитать количество существующих овец                                          8kui
################################################################################

# def count_sheeps(sheep):
#     a = sheep.count(True)
#     print(a)
#     return a


#  print(count_sheeps([True,  True,  True,  False,
#                     True,  True,  True,  True,
#                     True,  False, True,  False,
#                     True,  False, False, True,
#                     True,  True,  True,  True,
#                     False, False, True,  True]))


################################################################################
# Сколько раз нужно перемножить цифры числа, чтобы получить число из одной цифры   6kui
################################################################################

# def persistence(n):
#     result = 0
#     n = str(n)
#     while len(n) > 1:
#         x = 1
#         for figure in n:
#             x *= int(figure)
#         x = str(x)
#         result += 1
#         n = str(x)
#     return result


# print(persistence(39))


################################################################################
# Удаление строки из пробелов                                                       8kui
################################################################################

# def no_space(x):
#     x = x.split()
#     x = ''.join(x)
#     print(x)
#     return x

# def no_space2(x):
#     x = x.replace(' ', '')
#     print(x)
#     return x


# no_space('8 j 8   mBliB8g  imjB8B8  jl  B')
# no_space2('8 j 8   mBliB8g  imjB8B8  jl  B')


################################################################################
#  Дан массив имен, вернуть строку с именами через "," последние 2 через "&"         6kui
################################################################################

# def namelist(names):
#     d = []
#     for name in names:
#         d += (dict.values(name))
#     if len(names) == 0:
#         result = ""
#     elif len(names) == 1:
#         result = "".join(d)
#     else:
#         last = d.pop(-1)
#         result = ", ".join(d)+" & "+last
#     return result


# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {
#       'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
# namelist([{'name': 'Bart'}])


################################################################################
#  Сложить числа и вернуть строку с суммой в бинарном формате                        7kui
################################################################################

# def add_binary(a, b):
#     result = (bin(a+b).split("0b"))[1]
#     return result


# def add_binary2(a, b):
#     return format(a + b, 'b')


# print(add_binary2(6, 9))


################################################################################
#  Сложить числа и вернуть строку с суммой в бинарном формате                        7kui
################################################################################

# def high_and_low(numbers):
#     arr = []
#     numbers = numbers.split(" ")
#     for number in numbers:
#         number = int(number)
#         arr.append(number)
#     numbers = str(max(arr))+" "+str(min(arr))
#     return numbers


# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


################################################################################
#  Вернуть средний символ в строке (или 2)                                          7kui
################################################################################

# def get_middle(s):
#     if len(s) % 2 == 0:
#         symbol = s[len(s)//2-1]+s[len(s)//2]
#     else:
#         symbol = s[len(s)//2]
#     return symbol


# print(get_middle("test"))
# print(get_middle("testing"))


################################################################################
#  Калькулятор из функций     (seven(times(five())), 35)                            5kui
################################################################################

# def actions(num, action, num2):
#     if action == "+":
#         res = num+num2
#     elif action == "-":
#         res = num-num2
#     elif action == "*":
#         res = num*num2
#     else:
#         res = num//num2
#     return res


# def numerizer(num, action):
#     if action == "":
#         return num
#     else:
#         num2 = action[1]
#         action = action[0]
#         res = actions(num, action, num2)
#         return res


# def zero(action=""): return numerizer(0, action)
# def one(action=""): return numerizer(1, action)
# def two(action=""): return numerizer(2, action)
# def three(action=""): return numerizer(3, action)
# def four(action=""): return numerizer(4, action)
# def five(action=""): return numerizer(5, action)
# def six(action=""): return numerizer(6, action)
# def seven(action=""): return numerizer(7, action)
# def eight(action=""): return numerizer(8, action)
# def nine(action=""): return numerizer(9, action)


# def plus(num2): return ["+", num2]
# def minus(num2): return ["-", num2]
# def times(num2): return ["*", num2]
# def divided_by(num2): return ["/", num2]


# print(one(plus(one())))
# print(seven(times(five())))
# print(four(plus(nine())))
# print(eight(minus(three())))
# print(six(divided_by(two())))
