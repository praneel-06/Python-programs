prof={"name": "Praneel","age":18,"courses":["Math","Compsci"]}
print (prof.get("name"))
print(prof.get("phone","Invalid input"))#if key is not present, then 2nd string is printed
prof["phone"]="9949"#new keyvalue pair in dictionairy
prof["name"]="CHSK"#new value for already existing key "name"
print (prof)
print(prof.keys())
print(prof.values())#prints and returns all keys and values in the dictionairy respectively
num=len(prof)#number of keys in a dict
print(num)