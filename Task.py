# students=[]
# n=int(input("enter marks of the students"))
# k=1
# while k<=n:
#     marks=int(input("enter marks"))
#     if marks == -1:
#        print("programme stopped")
#        break
#     if marks<0 or marks>100:
#         print("Invalid marks")
#         continue
#     if marks>=80:
#        result="eligible for scholarship"
#     elif marks>=50:
#        result="Pass"
#     else: 
#         result="Fail"
#     students.append(result)

#     k = k + 1

# print("Student Results:")

# for result in students:
#     if result == "Fail":
#         pass

#     print(result)

# age = 20

# print(age >= 18 and age <= 60)
# print(age < 18 or age > 60)
# print(not(age == 20))

# a = 5
# b = 3

# print(a & b)
# print(a | b)

s = open("marks.txt", "w")
s.write("MRDUT CSE")
s.close()

s = open