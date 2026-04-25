
fruits=["apples", "bananas", "oranges"]


fruits.append("strawberries")
fruits.insert(2,"grapes")
fruits.remove("bananas")
fruits.pop(1)

# print(fruits)


indx = fruits.index("apples")

# print(indx)

# print(f" list of index is {"apples"}")







numbers = [1,2,2,3,4,4,5]
# list = list(set(numbers))
# print(list)


# list = list(dict.fromkeys(numbers))
# print(list)



list1 = [1,3,5]
list2 = [2,4,6]

complete_list = list(list1 + list2)
complete_list.sort()
print(complete_list)