n = int(input("Enter a positive integer n: "))

# Initialize variables
sum_of_numbers = 0
i = 1

# Use a while loop to calculate the sum
while i <= n:
    sum_of_numbers += i
    i += 1

# Display the result
print("The sum of the first", n, "natural numbers is:", sum_of_numbers)
