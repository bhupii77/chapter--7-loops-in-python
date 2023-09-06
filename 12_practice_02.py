#write a program to greet all the persons name in a list l1 and which start with S .  l1["harry","bhupii","sohail","uday","shivani"]

l1=["harry","bhupii","sohail","uday","shivani"]

for name in l1:
    if name.startswith("s"):
        print("Hello " + name) 