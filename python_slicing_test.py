my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract elements from index 2 to 5 (exclusive)
subset = my_list[2:5]
print(subset)  # Output: [2, 3, 4]

# Extract every second element from index 1 to 8
subset = my_list[1:8:2]
print(subset)  # Output: [1, 3, 5, 7]

# Omitting start and stop (copy the whole list)
copy_of_list = my_list[:]
print(copy_of_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negative indices can be used for counting from the end
subset = my_list[-3:]  # Last three elements
print(subset)  # Output: [7, 8, 9]

subset = my_list[1:4:2]  # all but the last three
print(subset)  # Output: [7, 8, 9]