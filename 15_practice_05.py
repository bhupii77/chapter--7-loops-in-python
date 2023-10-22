#Write a program to find sum of n natural numbers using while loop .
n = int(input('Enter a positive integer n:'))

sum_of_numbers:0

i = 1

while i <= n:
    sum_of_numbers +=i
    i+=1

#print(f'sum of first {n}natural number is {sum_of_numbers}')
print("The sum of the first", n, "natural numbers is:", sum_of_numbers)
    
