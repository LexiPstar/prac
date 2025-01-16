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

class Student(object):
    __table__name = 'sss'
    username=textwrap
    def __init__(self, name):