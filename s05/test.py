a = ["mohammad", "ali", "ahmad"]
b = ["nozari", "alavi", "ahmadi"]
for y,z in enumerate(a):
    print(y,z)

for i,(name, last_name) in enumerate( zip(a, b)):
    print(i,name, last_name)

