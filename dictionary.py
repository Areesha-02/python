
student_data={
    "name":"Areesha",
    "age": 19,
    "skills":["MS Office", "Python"]
}

student_data.update({"city":"Karachi"})

# student_data.pop("age")

# print(student_data.keys())
# print(student_data.values())
# print(student_data.items())

print(student_data)



copy_dict=student_data.copy()
print(copy_dict)