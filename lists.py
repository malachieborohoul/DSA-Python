fruits=["mango", "banana", "grape"]

# print("Enter a fruit name")
# done = True

# while done:
#     entry = input()
#     if entry == " ":
#         done = False
#     elif entry not in fruits:
#         fruits.append(entry)
#     else:
#         for fruit in fruits:
#             if fruit == entry:
#                 print('{0} is already in the list'.format(fruit))        
# print(fruits)


phones =["iphone", "samsung", "huawei"]

phones.append("techno")


print(phones)

# 
alpha = [1,2,3]

beta=alpha

beta += [4,5]
   
# The reassignation breaks the alias between alpha and beta
beta = beta + [6,7]
print(beta)
