# message = input("主题: ")
# print('-'*50)
# while True:
#     admin = input("用户名: ")
#     context = input("评论: ")
#     context = context.strip()
#     if len(context) != 0:
#         if len(context) <= 20:
#             context = context.replace('sss', '***')
#             print('\t{}发表的评论是：\n\t{}'.format(admin, context))
#         else:
#             print("评论超过二十字")
#     else:
#         print('不能为空！')
#     pass


# cus = [['牛奶', 3, 6], ['火腿肠', 5, 2], ['辣条', 4, 3]]
# sums = cus[0][2] * cus[0][1] + cus[1][2] * cus[1][1] + cus[2][2] * cus[2][1]
# print(sums)

# container = []
# flag = True
# while flag:
#     name = input("Enter your name: ")
#     price = float(input("Enter your price: "))
#     total = int(input("Enter your total price: "))
#     goods = [name, price, total]
#     container.append(goods)
#     answer = input("Do you want to add another one?(y/n): ")
#     if answer.lower() == 'n':
#         flag = False
# print('-' * 20)
# print('名称\t价格\t数量')
# for goods in container:
#     print('{}\t{}\t{}'.format(goods[0], float(goods[1]), int(goods[2])))


# sd = ['aa', 'bb', 'bb', 'dd', 'ee', 'ff', 'ff', 'hh', 'ii', 'jj']
# for i in sd:
#     if i == 'bb' or 'ff':
#         sd.remove(i)
#         i = i
# print(sd)
# n = 0
# while n < len(sd):
#     if sd[n] == 'bb':
#         sd.remove('bb')
#         n = n
#     else:
#         n += 1
# print(sd)

# sr = []
# for i in range(9, 10, 20):
#     sr.append(i)
#     print(sr)

# asd = 'addenda'
# i = 'ade'
# if i in asd:
#     print(i)

# class Student(object):
#     __table__name = 'sss'
#     username = 'index=text(ss0)'
#
#
# def __init__(self, name):
#     self.name = name


# i = 1
# sum = 0
# while i < 101:
#     sum += i
#     i += 1
# print(sum)
# i = 100
# sum = (1 + i) * i / 2
# print(sum)


# def generate_pascals_triangle(num_rows):
#     triangle = []
#     for row_num in range(num_rows):
#         # 每一行的第一个元素总是1
#         row = [1]
#         if triangle:
#             # 获取上一行
#             last_row = triangle[-1]
#             # 计算当前行的中间元素
#             row += [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)]
#             # 每一行的最后一个元素总是1
#             row.append(1)
#         triangle.append(row)
#     return triangle
#
#
# def print_pascals_triangle(triangle):
#     for row in triangle:
#         print("  ".join(map(str, row)).center(len(triangle[-1]) * 3))
#
#
# # 生成并打印杨辉三角
# num_rows = int(input())
# triangle = generate_pascals_triangle(num_rows)
# print_pascals_triangle(triangle)

num = 222
char = 'abcd'
print(char)

