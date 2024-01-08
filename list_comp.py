# squares =[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# square2 = [i**2 for i in range(1,11)]
# print(square2)

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# negative2 = [-i for i in range(1,11)]
# print(negative2)

# names = ['abdullah','dani','hamza']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

# new2 = [name[0] for name in names ]
# print(new2)


# def reverse_strings(l):
#     return[name[::-1]for name in l]
# print(reverse_strings(['abc','xyz','pqr']))

# def new_str(l):
#     new_list=[]
#     for name in l :
#         new_list.append(name[::-1])
#     return new_list
# print(new_str(['abc','pqr','xyz']))

odd_nums = [i for i in range(1,11) if i%2 != 0]
even_nums = [ i for i in range(1,11) if i%2 == 0]
print(even_nums)
print(odd_nums)

square = [i**2 for i in range(1,11)]
print(square)
