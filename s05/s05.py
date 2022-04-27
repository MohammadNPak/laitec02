# a = {2,3,3,3,3,4,4,4,4,5}
# b = [1,2,3]
# a.update([8,9])

# print(type(a))

# a = list(set(map(int,input().split())))
# print(a)


# a = 2
# b = a
# a = 3
# print(a, b)
# print(id(a), id(b))

# a = [1,2,3]
# b = a.copy()
# a.pop()
# print(a, b)
# print(id(a), id(b))

# dict

# key:value
# a = {"name": "mohammad", "age": 10, 2: 5}
# print(a[2])

# print(hash((1,2,3)))

# command == add

# [
#   {"id":1,"name":"mohammad",...},
#   {"id":2,"name":"ali",...},
# ]
students = []
while True:
    command = input("command: ")
    if command == "add":
        if not students:
            id = 1
        else:
            id = students[-1]["id"]+1
        name = input(f"please enter student #{id} name:")
        last_name = input(f"please enter student #{id} last name:")
        age = int(input(f"please enter student #{id} age:"))
        student = {"id": id, "name": name, "last_name": last_name, "age": age}
        students.append(student)
    elif command == "exit":
        break
    elif command == "show all":
        for student in students:
            print(student)

    elif command == "remove":
        key = input("enter remove key:")
        value = input("enter remove value:")
        for i, student in enumerate(students):
            if student[key] == value:
                remove_index = i
                break
        students.pop(remove_index)
