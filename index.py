# my_list = [2, 3, 2, 4, 4, 5]
# unique_list = []

# for i in range(len(my_list)):
#     is_unique = True
#     for j in range(len(unique_list)):
#         if my_list[i] == unique_list[j]:
#             is_unique = False
#             break
#     if is_unique:
#         unique_list.append(my_list[i])

# print(unique_list)


# my_list = [2, 3, 2, 4, 4, 5]
# greate_Num = 0

# for i in range(len(my_list)):
#     is_unique = True
#     for j in range(len(my_list)):
#         if my_list[j] > my_list[i]:
#             greate_Num = my_list[j]
  

# print(greate_Num)

# my_list = [10, 1, 2, 3, 2, 7, 0 , 9, 4, 5]
# small_Num = my_list[0]  

# for i in range(1, len(my_list)):
#     if my_list[i] < small_Num:
#         small_Num = my_list[i]

# print(small_Num)


my_list = [2, 3, 2, 4, 4, 5,5,6,0,0,8]
unique_list = []
count=0

for i in range(len(my_list)):
    is_unique = True
    for j in range(len(unique_list)):
        if my_list[i] == unique_list[j]:
            is_unique = False
            count+=1
            break
        
           
    if is_unique:
        unique_list.append(my_list[i])

print(unique_list)
print(count)


       
