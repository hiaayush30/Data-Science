import math

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

# Problem 9: Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

li = []
for i in range(2000,3001):
    if i % 7 == 0 and i % 5 != 0:
        li.append(str(i))
print(",".join(li))

# Problem 10: Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a space-separated sequence on a single line.

for i in range(2000, 3201):
    num = i
    all_even = True
    while num > 0:
        if (num % 10) % 2 != 0:
            all_even = False
            break
        num = num // 10
    if all_even:
        print(i, end=",")

# Problem 11: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# The numbers after the direction are steps.
# ! means robot stop there.
# Please write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.

sequence = []

while True:
    user_input = input("Enter command:")
    if user_input == "!":
        break
    sequence.append(user_input)

x_travelled = 0
y_travelled = 0
for command in sequence:
    [direction, distance] = command.split()
    distance = int(distance)
    match direction:
        case "UP":
            y_travelled = y_travelled + distance
        case "DOWN":
            y_travelled = y_travelled - distance
        case "RIGHT":
            x_travelled = x_travelled + distance
        case "LEFT":
            x_travelled = x_travelled - distance
        case _:
            print("Invalid command!")

# now we have the final x and y coordinates
print("x:",x_travelled)
print("y:",y_travelled)
print(f"distance travelled is {math.floor(((x_travelled**2)+(y_travelled**2))**0.5)}")

# Problem 12:Write a program to print whether a given number is a prime number or not

num = int(input("Enter num:"))
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("It is a prime number")
else:
    print("It is not a prime number")

# Problem 13:Print all the Armstrong numbers in a given range.

lower = int(input("Enter lower limit of range:"))
upper = int(input("Enter upper limit of range:"))

for i in range(lower,upper+1):
    sum = 0
    n = i
    while(n>0):
        sum = sum + (n%10)**3
        n = n//10
    if sum == i:
        print(i)

# Problem 14:Calculate the angle between the hour hand and minute hand.

h = int(input("Enter hour hand position:"))
m = int(input("Enter minute hand position:"))

angle = (h - m) * 30

if angle < 0:
    angle = angle * -1
if angle > 180:
    angle = angle - 180
print(angle," deg")

# Problem 15:Reactangles overlapping or not

lx1 = int(input("Enter x coordinate of left top of ractangle 1:"))
ly1 = int(input("Enter y coordinate of left top of ractangle 1:"))
rx1 = int(input("Enter x coordinate of right bottom of ractangle 1:"))
ry1 = int(input("Enter y coordinate of right bottom of ractangle 1:"))

lx2 = int(input("Enter x coordinate of left top of ractangle 2:"))
ly2 = int(input("Enter y coordinate of left top of ractangle 2:"))
rx2 = int(input("Enter x coordinate of right bottom of ractangle 2:"))
ry2 = int(input("Enter y coordinate of right bottom of ractangle 2:"))

# If one rectangle is to the right of the other, they do not overlap.
if lx1 >= rx2 or lx2 >= rx1:
    print("they don't overlap")

# If one rectangle is entirely above the other, they do not overlap.
if ly1 <= ry2 or ly2 <= ry1:
    print("they don't overlap")

# Otherwise, they must overlap.
print("They overlap")
