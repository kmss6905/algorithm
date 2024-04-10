a = input()
b = ""
for i in a:
    if i.isupper():
        b += i.lower()
    
    if i.islower():
        b += i.upper()
print(b)