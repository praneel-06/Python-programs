l=["Hello, my name is Praneel!","Today there's a match between India,Aus."]
l1=[]
string=""
for sentence in l:
    for char in sentence:
        if(char.isdigit() or char.isalpha() or char==" "):
            string=string+char
            continue
    l1.append(string)
    string=""
print(l1)
