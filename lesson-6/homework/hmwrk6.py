#2
n = int(input("Enter a number between 1 and 20: "))

if 1 <= n <= 20:
    for i in range(n):
        print(i ** 2)
else:
    print("Invalid input. Please enter a number from 1 to 20.")

#3.1
i = 1
while i <= 10:
    print(i)
    i += 1
#3.2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
#3.3
num = int(input("Enter number: "))
total = 0
i = 1

while i <= num:
    total += i
    i += 1

print("Sum is:", total)
#3.4
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)

#3.5

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if 50 < num < 500:
        print(num)

#3.6
num = 75869
count = 0

while num != 0:
    num //= 10
    count += 1

print("Total digits:", count)

#3.7

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

#3.8

list1 = [10, 20, 30, 40, 50]

i = len(list1) - 1
while i >= 0:
    print(list1[i])
    i -= 1

#3.9
for i in range(-10, 0):
    print(i)

#3.10
for i in range(5):
    print(i)
print("Done!")

#3.11

start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)
#3.12

n_terms = 10
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n_terms:
    print(n1, end='  ')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

#3.13

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")

#4
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    diff = (c1 - c2) + (c2 - c1)
    result = []
    for key, count in diff.items():
        result.extend([key] * count)
    return result
list1_input = input("Enter first list of numbers separated by space: ")
list2_input = input("Enter second list of numbers separated by space: ")
list1 = list(map(int, list1_input.split()))
list2 = list(map(int, list2_input.split()))
result = uncommon_elements(list1, list2)
print("Uncommon elements:", result)
