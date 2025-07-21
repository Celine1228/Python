#1
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
user_input = input("Enter a year: ")

try:
    year = int(user_input)
    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Please enter a valid integer year.")

#2

n = int(input().strip())

if n % 2 == 1:                     
    print("Weird")
elif 2 <= n <= 5:                 
    print("Not Weird")
elif 6 <= n <= 20:                
    print("Weird")
else:                              
    print("Not Weird")

#3
def even_numbers_with_if(a, b):
    if a > b:
        return []
    elif a % 2 == 0:
        return [a] + even_numbers_with_if(a + 2, b)
    else:
        return even_numbers_with_if(a + 1, b)
print(even_numbers_with_if(3, 10))

def even_numbers_without_if(a, b):
    return list(range(a + a % 2, b + 1, 2))
print(even_numbers_without_if(3, 10))
