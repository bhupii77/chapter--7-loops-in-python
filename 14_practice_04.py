# write a program to find whether the given number is prime or not ?

num = int(input('Enter the number: '))

prime = True
for i in range(2 ,num) :
    if (num%i == 0):
        prime = False 
        break
if prime :
    print('the number is prime ')

else:
    print('the number is not prime')        
    