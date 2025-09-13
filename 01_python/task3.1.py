# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

n = int(input("Enter n:"))
x = int(input("Enter x:"))

sum = 1

for i in range(2, n + 1):
    sum = sum + (x**i) / i

print(sum)

# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690.

n = int(input("Enter n:"))
sum = 0
to_add = 2
while n != 0:
    if n == 1:
        print(to_add)
    else:
        print(to_add, end="+")
    sum = sum + to_add
    to_add = int(str(to_add) + "2")
    n = n - 1
print(sum)

# Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                print(i,j,k,l)


# Problem 9: Write a program that will take a decimal number as input and prints out
# the binary equivalent of the number

n = 14
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = int(n / 2)

print(int(binary))
