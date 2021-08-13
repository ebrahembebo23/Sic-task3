# ask user to enter the size of the list
li_size = int(input("How many numbers are in the list : "))
# Define "number entered" list and list of final result
numbers_li = []
final_li = []
# loop to ask user to enter items of list depended on size of list
for i in range(0, li_size):
    numbers_li.append(int(input("Enter list item {} : ".format(i + 1))))
# ask user to enter the number that divisible number of
n = int(input("Enter divider : "))
# loop that make the equation
for i in range(0, li_size):
    if numbers_li[i] % n == 0:
        final_li.append(numbers_li[i])
# printing the final result
print("Numbers that are divisible by {} is : ".format(n), final_li)
