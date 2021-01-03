"""

You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]
Input:
Take a list as an input from the user
[5, 4, 1]
Output:
[1, 4, 5]
[1, 4, 5]
[1, 4, 5]
"""
try:
    print("Enter element if you want to stop enter stop")
    items = []
    while True:
        element = int(input())
        items.append(element)
except:
    print(items)
items1 = items.copy()
print(items1[::-1])
items1 = items.copy()
items1.reverse()
print(items1)
items1 = items.copy()
for i in range(0, (len(items1) // 2)):
    items1[i], items1[len(items1) - i - 1] = items1[len(items1) - i - 1], items1[i]

print(items1)
