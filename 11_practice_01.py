#question 1 : write a program to print multiplication table of a given number using for loop




num = int(input("Enter the number"))
for i in range(1,11):
    #print(str(num)+ "x" + str(i) + "=" + str(i*num))
    print(f"{num}x{i}={num*i}")