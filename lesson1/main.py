from dataclasses import replace

my_string = "Мене звати Артем"
print(type(my_string))
my_integer = 28
print(type(my_integer))
my_float = "0.7"
print(type(my_float))
my_bool = "True"
print(type(my_bool))
my_list =  [2, 4, 6]
print(type(my_list))
my_dict = {"ім'я": "Артем", "вік": 28, "місто": "Київ"}
print(type(my_dict))
my_tuple = (2, 4, 6)
print(type(my_tuple))
my_none = None
print(type(my_none))

num_1 = 2
num_2 = 4
num_3 = num_1 + num_2
print(num_3)


num_1 = 2
num_2 = 4
num_3 = num_1 * num_2
print(num_3)


num_1 = 2
num_2 = 4
num_3 = num_2 / num_1
print(num_3)


num_1 = 2
num_2 = 4
num_3 = num_1 // num_2
print(num_3)

num_1 = 2
num_2 = 4
num_3 = num_1 % num_2
print(num_3)

num_1 = 2
num_2 = 4
print(num_1 > num_2)

num_1 = 2
num_2 = 4
print(num_1 < num_2)

num_1 = 2
num_2 = 4
print(num_1 > num_2 and num_1 < num_2)

num_1 = 2
num_2 = 4
print(num_1 > num_2 or num_1 < num_2)

lst = [2, 3, 4, 5]
dct = {'name': 'ARTEM', 'age': 28, 'from': 'KYIV'}
name = 'ARTEM'
tpl = ('n', 'm', '28')

print(2 in dct)

lst = [28, 3, 4, 5]
dct = {'name': 'ARTEM', 'age': 28, 'from': 'KYIV'}
name = 'ARTEM'
tpl = ('name' == name and dct[age] in lst)

num_str = 125
txt = str(num_str)

message = 'Hi, my name is Python!'
text= message.replace( 'y', 'o').replace('i', '1')
print(text)

split_test = 'This is a split test'
split = split_test.split()
join_result = ' '.join(split)

text =  'string_join'
lengh = len(text)
print(lengh)

list_append = [1, 2, 3]
list_append.append([5])
list_append.append(4)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

list_extend = [4, 5, 6]
index_of_6 = list_extend.index(6)
print(index_of_6)

list_append = [1, 2, 4]
length = len(list_append)
print(length)

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
dict_test = dict_test.keys()
print(dict_test)
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
dict_test = dict_test.values()
print(dict_test)

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.items())