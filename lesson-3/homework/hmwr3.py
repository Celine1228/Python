
# 1
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print("Third fruit:", fruits[2])  

# 2.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)

# 3.
numbers = [10, 20, 30, 40, 50, 60]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
extracted = [first, middle, last]
print("Extracted elements:", extracted)

# 4. 
movies = ["Inception", "Matrix", "Interstellar", "Gladiator", "Titanic"]
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)

# 5. 
cities = ["London", "New York", "Tokyo", "Paris"]
is_paris = "Paris" in cities
print("Is Paris in the list?", is_paris)

# 6. 
nums = [1, 2, 3]
duplicated = nums * 2
print("Duplicated list:", duplicated)

# 7.
swap_list = [9, 8, 7, 6, 5]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("Swapped list:", swap_list)

# 8. 
num_tuple = tuple(range(1, 11))  
sliced = num_tuple[2:7]  
print("Sliced tuple (3 to 7):", sliced)

# 9. 
colors = ["red", "blue", "green", "blue", "blue", "yellow"]
blue_count = colors.count("blue")
print("Number of times blue appears:", blue_count)

# 10.
animals = ("cat", "dog", "lion", "tiger")
lion_index = animals.index("lion")
print("Index of 'lion':", lion_index)

# 11. 
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

# 12.
list_sample = [10, 20, 30, 40]
tuple_sample = (5, 15, 25)
print("Length of list:", len(list_sample))
print("Length of tuple:", len(tuple_sample))

# 13.
tuple_numbers = (1, 2, 3, 4, 5)
converted_list = list(tuple_numbers)
print("Converted list:", converted_list)

# 14. 
num_values = (12, 45, 3, 88, 23)
print("Maximum:", max(num_values))
print("Minimum:", min(num_values))

# 15.
words = ("hello", "world", "python", "rocks")
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)

