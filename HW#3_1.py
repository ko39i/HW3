1.
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

2
list.append(lst_d, 4)
list.append(lst_d, 5)
print(id(lst_d))

3
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

4
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

5
print("Anna has {} apples and {} peaches.".format(4, 5))

6
print("Anna has {0} apples and {1} peaches.".format("red", "yellow"))

7
print("Anna has {ap} apples and {pe} peaches.".format(pe="red", ap="yellow"))

8
print("Anna has {0:5} apples and {1:3} peaches.".format(5, 7))

9
fruit1 = "green"
fruit2 = "orange"
print(f"Anna has {fruit1} apples and {fruit2} peaches.")

10
fruit1 = "green"
fruit2 = "orange"
print("Anna has %s apples and %s peaches." % (fruit2, fruit1))

11
a = "red"
p = "green"
data_dict = {"fruit1": a, "fruit2": p}
print("Anna has %(fruit1)s apples and %(fruit2)s peaches." % data_dict)

12
list_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comp)

13
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

14
dict_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comp)

15
dict_comp = {num: num ** 2  if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comp)



16
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
print(d)

17
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)

18

foo = lambda x, y: x if x < y else y

print(foo(4, 5))
19

def foo(x, y, z):
    if y < x and x > z :
        return z
    else:
        return y
print(foo(4, 5, 2))

20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

21
print(sorted(lst_to_sort, reverse=True))

22
lst_new = list(map(lambda x: x * 2, lst_to_sort))
print(lst_new)

23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_C = list(map(pow, list_A, list_B))
print(lst_C)

24
import functools
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
sum = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(sum)

25
lst_flt = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(lst_flt)

26

b = range(-10, 10)
lst_negative = list(filter(lambda elem: elem < 0, b))
print(lst_negative)

27
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x == x, list_1 and list_2))
print(list_3)
