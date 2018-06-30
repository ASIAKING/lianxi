my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
for key in my_dict:
  print (key, my_dict[key])
# 构建符合某种规律的列表
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
print(even_squares)
# 列表切片语法 起点终点步数
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l[2:9:2])

