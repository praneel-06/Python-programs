prof={"name": "Praneel","age":18,"courses":["Math","Compsci"]}


for ele,name in prof.items():
    print(ele,name)
print("****************")
for key in prof: #since only prof was mentioned, it prints keys
    print(key)
print("****************")
for values in prof.values():
    print(values)
