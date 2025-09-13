# Problem 8: Take a user input as integer N. Find out the sum from 1 to N.
# If any number if divisible by 5, then skip that number.
# And if the sum is greater than 300, don't need to calculate the sum further more.
# Print the final result.
num = int(input("Enter a number:"))
sum = 0
for i in range(1, num + 1):
    if i %5 != 0:
        if sum + i > 300:
            break
        sum = sum + i
print(sum)
