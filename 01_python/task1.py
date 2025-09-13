print("Data", "Science", end="-by-", sep="-")
print("CampusX")


# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2

heads = input("Enter number of heads -> ")
legs = input("Enter number of legs -> ")

if not heads.isdigit() or not legs.isdigit():
    print("Enter a valid input!")
    exit()

# dogs + chickens = heads
# 4*dogs + 2*chcikens = legs

heads = int(heads)
legs = int(legs)
dogs = (legs - 2 * heads) / 2
chickens = heads - dogs

print(f"dogs -> {int(dogs)}")
print(f"chickens -> {int(chickens)}")

# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
num = int(input("Enter n: "))
sum_squares = (num * (num + 1) * (2 * num + 1)) / 6
print(f"The sum of squares of first {num} numbers is {sum_squares}")


# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

a = int(input("Enter first term: "))
b = int(input("Enter second term: "))
d = b - a
n = int(input("Enter the term you want: "))

print(f"The term at position {n} will be {a+(n-1)*d}")

# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
n1 = int(input("Enter numerator of first number:"))
d1 = int(input("Enter denominator of first number:"))
n2 = int(input("Enter numerator of second number:"))
d2 = int(input("Enter denominator of second number:"))

num = d2 * n1 + d1 * n2
den = d2 * d1
print("{}/{}".format(num, den))

# Q10:- factorial of a number
reversed = 0
num = 12345
while num > 0:
    reversed = (reversed * 10) + num % 10
    num = num // 10
print(reversed)