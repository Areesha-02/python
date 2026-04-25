
mixed_tuple=(1, "Hello", 3.67, True)

print(mixed_tuple.count(1))
print(mixed_tuple.count("Hello"))
print(mixed_tuple.index(1))
print(mixed_tuple.index("Hello"))

print(len(mixed_tuple))




# changing list into tuple

list = [1,2,3,4,5]

tuple=tuple(list)
print(tuple)