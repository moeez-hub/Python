size = int(input("Enter the size of the list: "))
my_list = []
for i in range(size):
    my_list.append(str(input()))
print("The elements in the list are:")
print(*my_list)