

#OLD VERSION, New Version is O(m)

# num_of_operations = int(input())

# for i in range(num_of_operations):
#     operations = [x.lower() for x in input()]
#     arr_length = int(input())
#     arr = [x for x in input().strip('[]').split(',')]

#     # Outer Cases
#     if arr_length == 0 and 'd' in operations:
#         print("error")

#     else:
    
#         for operation in operations:
#             match (operation):
#                 case 'r':
#                     arr.reverse()
#                 case 'd':
#                     if arr_length == 0:
#                         print("error")
#                         break
#                     arr.pop(0)
#                 case _:
#                     print("Undefined Case")
#                     exit()
#     print(list(map(int, arr)))
            

# In this solution, I am using an orientation bool variable and popping integers in constant speed, not relying on reversing the array.
# This solution only reverses the array once if the bool variable is false, and also uses slicing for faster computation 
# Also, switched input and output to stdin and stdout for faster computation

# from sys import stdin, stdout

# line = stdin.readline

# for i in range(int(stdin.readline())):
#     orientation = True
#     is_error = False
#     drop_front = 0
#     drop_end = 0
#     operations = [x.lower() for x in stdin.readline()]
#     arr_length = int(stdin.readline())
#     arr = [int(x) for x in stdin.readline().strip()[1:-1].split(',')]
#     if arr:
#         for operation in operations:
#             if operation == 'r': orientation = not orientation
#             elif operation == 'd':
#                 if orientation : drop_front += 1
#                 else: drop_end += 1
#             if drop_front + drop_end > arr_length : 
#                 is_error == True
#                 break
#         if is_error:
#             stdout.write("error\n")
#         else:
#             arr = arr[drop_front:arr_length-drop_end]
#             if not orientation : arr.reverse()
#             stdout.write(str(arr).replace(' ', ''))
#             stdout.write("\n")
#     else:
#         if 'd' in operations : stdout.write("error\n")
#         else : stdout.write("[]\n")


from sys import stdin, stdout

line = stdin.readline

for i in range(int(line())):
    orientation = True
    is_error = False
    drop_front = 0
    drop_end = 0
    operations = [x.lower() for x in line()]
    arr_length = int(line())

    # array intake
    arr_input = line().strip()
    if arr_input == "[]":
        if 'd' in operations:
            stdout.write("error\n")
        else:
            stdout.write("[]\n")
    else:
        arr = list(map(int, arr_input[1:-1].split(',')))

        # reading operations
        for operation in operations:
            if operation == 'r':
                orientation = not orientation
            elif operation == 'd':
                if orientation:
                    drop_front += 1
                else:
                    drop_end += 1
                if drop_front + drop_end > arr_length:
                    is_error = True
                    break
        # output
        if is_error:
            stdout.write("error\n")
        else:
            arr = arr[drop_front:arr_length - drop_end]
            if not orientation:
                arr.reverse()
            stdout.write(str(arr).replace(' ', '') + "\n")