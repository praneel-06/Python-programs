message="Hello world"

print(len(message))
print(message.count("a"))
print(message.upper())#can use lower() command also
print(message[2:7])#called as slicing 

new_message=message.replace("world","universe")
print(new_message)

greeting="Good Morning"

greet= message + ", " + greeting + " sunny day eh?"
print(greet) #instead of this long code we can use format operation to reduce the code

greet1= "{}, {} sunny day eh?".format(message,greeting)
print(greet1)
#to furthur simplify
greet2 =f"{message}, {greeting} sunny day eh?"
print(greet2)
#print(dir(message)) all the different functions you can do with str var(names only)
#print(help(data type)) gives us all the different (detailed notes on methods)
#print(help(str.lower)) gives specific details on asked function