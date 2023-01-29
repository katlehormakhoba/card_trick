# # Import the random module
# import random

# # Create an array containing 21 unique numbers
# numbers = list(range(1, 22))


# array1 = []
# array2 = []
# array3 = []

# random.shuffle(numbers)
# print(f"Original array: {numbers}")

# # Iterate over the numbers array by 3
# for x in range(0, 21, 3):
#     array1.append(numbers[x])
#     array2.append(numbers[x + 1])
#     array3.append(numbers[x + 2])


# # Display the arrays to the user
# print("\nArray 1:", array1)
# print("Array 2:", array2)
# print("Array 3:", array3)

# # Ask the user to pick an array
# selected_array = input("\nWhich array is your number in? ")


# # Print the selected array
# if selected_array == "1":
#     numbers = array2 + array1 + array3
#     print("You selected array 1:", array1)
# elif selected_array == "2":
#     numbers = array1 + array2 + array3
#     print("You selected array 2:", array2)
# elif selected_array == "3":
#     print("You selected array 3:", array3)
#     numbers = array1 + array3 + array2
# else:
#     print("Invalid selection")



# print(f"Original array: {numbers}")
# array1 = []
# array2 = []
# array3 = []
# for x in range(0, 21, 3):
#     array1.append(numbers[x])
#     array2.append(numbers[x + 1])
#     array3.append(numbers[x + 2])


# # Display the arrays to the user
# print("\nArray 1:", array1)
# print("Array 2:", array2)
# print("Array 3:", array3)

# # Ask the user to pick an array
# selected_array = input("\nWhich array is your number in? ")


# # Print the selected array
# if selected_array == "1":
#     numbers = array2 + array1 + array3
#     print("You selected array 1:", array1)
# elif selected_array == "2":
#     numbers = array1 + array2 + array3
#     print("You selected array 2:", array2)
# elif selected_array == "3":
#     print("You selected array 3:", array3)
#     numbers = array1 + array3 + array2
# else:
#     print("Invalid selection")

# print(f"Original array: {numbers}")
# array1 = []
# array2 = []
# array3 = []
# for x in range(0, 21, 3):
#     array1.append(numbers[x])
#     array2.append(numbers[x + 1])
#     array3.append(numbers[x + 2])


# # Display the arrays to the user
# print("\nArray 1:", array1)
# print("Array 2:", array2)
# print("Array 3:", array3)

# # Ask the user to pick an array
# selected_array = input("\nWhich array is your number in? ")


# # Print the selected array
# if selected_array == "1":
#     numbers = array2 + array1 + array3
#     print("You selected array 1:", array1)
# elif selected_array == "2":
#     numbers = array1 + array2 + array3
#     print("You selected array 2:", array2)
# elif selected_array == "3":
#     print("You selected array 3:", array3)
#     numbers = array1 + array3 + array2
# else:
#     print("Invalid selection")

# print(f"Original array: {numbers}, {numbers[10]}")


#----------------------------------------------------------------

# Import the random module
# Import the random module
import random

def split_main_to_arrays():
    # Iterate over the numbers array by 3
    for x in range(0, 21, 3):
        array1.append(numbers[x])
        array2.append(numbers[x + 1])
        array3.append(numbers[x + 2])

# Display the arrays to the user
def display_new_arrays():
    print("\nArray 1:", array1)
    print("Array 2:", array2)
    print("Array 3:", array3)
    # Ask the user to pick an array
    selected_array = input("\nWhich array is your number in? ")
    if selected_array not in ["1","2","3"]:
         print("Invalid selection. Please try again.")
         return display_new_arrays()

    return int(selected_array)

# Print the selected array
def sort_arrays(selected_array):
    if selected_array == 1:
        numbers = array2 + array1 + array3
        print("You selected array 1:", array1)
    elif selected_array == 2:
        numbers = array1 + array2 + array3
        print("You selected array 2:", array2)
    elif selected_array == 3:
        print("You selected array 3:", array3)
        numbers = array1 + array3 + array2
    else:
        print("Invalid selection")
    return numbers


# Create an array containing 21 unique numbers
numbers = list(range(1, 22))

random.shuffle(numbers)
print(f"Original array: {numbers}")


count = 0
while count < 3:
  # code block to be executed
    array1 = []
    array2 = []
    array3 = []

    split_main_to_arrays()
    selected_array = display_new_arrays()
    numbers =  sort_arrays(selected_array)

    count += 1

print(f"Original array: {numbers}, {numbers[10]}")


