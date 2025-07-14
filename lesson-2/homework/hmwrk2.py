#1
year=int(input("iltimos tugilganyilingizni kiriting    "))
name=input("iltimos ismingizni kiriting    ")
yourage=2025-year

print(f"{name} sizni yoshingiz {yourage}")

#2
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

#3
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[::-2])

#4
txt = "I'am John. I am from London"
parts=txt.split('from')
area=parts[1]
print(area)

#5
txt=input('Enter a string: ')
reversedv=(txt[::-1])
print('reversed code: ', reversedv)

#6
import re

txt=input("Enter the sentence ")
count=len(re.findall(r'[aeiouAEIOU]', txt))
print("Number of vowels:", count)

#7
nums = input("Enter numbers separated by space: ").split()
nums = [int(num) for num in nums]
print("Maximum value:", max(nums))

#8
word=input("so'zni kirit: ")
if word==word[::-1]:
    print("palindrome")
else: print('not a p')

#9
email = input("Enter your email address: ")
parts = email.split('@')

if len(parts) == 2:
    domain = parts[1]
    print("Domain:", domain)
else:
    print("Invalid email format.")

#10
import random
import string
length = int(input("Enter the desired password length: "))
all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_chars) for _ in range(length))
print("Generated Password:", password)


