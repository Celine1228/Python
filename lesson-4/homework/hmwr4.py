#1
my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)

desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)

#2
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30  
print("Updated dictionary:", sample_dict)

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)

#4
n = 5
squares_dict = {}
for x in range(1, n + 1):
    squares_dict[x] = x * x
print(squares_dict)

#5
n = 15
squares_dict = {}
for x in range(1, n + 1):
    squares_dict[x] = x * x
print(squares_dict)

#Set exercises
#1
fruits = {"apple", "banana", "cherry"}
print("My fruit set is:", fruits)

#2
fruits = {"apple", "banana", "cherry"}
print("Iterating through the set:")
for fruit in fruits:
    print(fruit)

#3
my_set = {"apple", "banana"}
my_set.add("cherry")
my_set.update(["orange", "grape"])
print("After adding:", my_set)

#4
my_set = {"apple", "banana", "cherry", "orange"}
my_set.remove("banana")
print("Set after removal:", my_set)

#5
my_set = {"apple", "banana", "cherry"}
if "banana" in my_set:
    my_set.remove("banana")
print("Updated set:", my_set)














