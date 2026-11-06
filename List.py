# nums_list = [10,20,3040,50,60,70,80]

# #Accessabiliy

# print(nums_list[0])
# print(nums_list[2])
# print(nums_list[:])

# # List data structures characteristics

# #Ordered
# fruits = ["Apple","Banana","Mango"]
# print(fruits[0])

# # Mutable
# fruits = ["Apple","Banana","Mango"]
# fruits[1] = "Orange"
# print(fruits)

# # Allows duplicate values
# numbers = [10,20,10,30]
# print(numbers)

# #Can store diferent data types
# data = [101,"Python",85.5,True]
# print(data)

# #Common list operations
# numbers = [10,20,30,40]
# print(len(numbers))

# # Add an element

# # Append
# numbers = [10,20,30]
# numbers.append(40)
# print(numbers)

# # Insert
# numbers = [10,20,30]
# numbers.insert(1,20)
# print(numbers)

# Slicing

numbers = [10,20,30,40,50]

# Basic slicing 
print(numbers[1:4])

# From beginning to a position 
print (numbers[:4])

# From a position to end
print (numbers[2:])

# Entire list
print(numbers[:])

# Using step
print(numbers[::-2])

# Reverse step
print(numbers[::-1])


# Nested list

matrix = [[1,2],[3,4],[5,6]]
print(matrix)

# Example Program

students=["YAMINI","GREESHMA","JAHNAVI","LAKSHMAN","SARAVANA","SANJANA","TEJA","CHERRY"]

students.append("PAPA")
students.insert(2,"RUTHVIK")
students.remove("YAMINI")
del students[3]
students.pop()

print("Student List:")
for s in students:
    print(s)
    print(len(students))