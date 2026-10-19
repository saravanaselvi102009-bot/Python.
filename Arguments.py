'''
#Types of arg

1.Positional
2.Keyword
3.Default
4.Variable
'''

#Positional

# def greet(name,wish):
#     print("Hello",name,wish)

# greet('good evng','avinash') #If gvng<--->avinash reverse the value

# def sum_sub(a,b):
#     sum = a+b
#     sub = a - b
#     result = sum , sub
#     print(result)
# sum_sub(100,500)
# sum_sub(500,100)


# #Keyword arg

# def greet(name,wish):
#     print("Hello",name,wish)

# greet(name="Srikhar",
# wish="good afn")
# greet(wish='good afn',
# name='srikhar')
#greet(name='Srikhar','good afn') #Invalid   


# def greet(name,age,city):
#     print('Hello',name,age,city)

# greet(name='Saravana',
#       age=17,
#       city='Tirupati')

#Default

# def greet(name='ravi',age=25):
#     print("Hello",name,age)
# greet()
 
#def f(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
#     f(3,2) #3,2,4,8  --> Positional with default
#     f(10,20,30,40) # 10,20,30,40 --> Positional arg
#     f(25,50,arg4=100)  #25,50,4,100  --> Positional with default
#     f(arg4=2,arg1=3,arg2=4)  # 3,4,4,2 --> Keyword arg
#     f() #error
#     f(4,5,arg2=6)   # Error
#     f(arg3=10,arg4=20,30,40) # Syntax error
#     f(4,5,arg3=5,arg5=6) # Type error

# def f1(**a):
#     print(a)
#     print(type(a))
# f1(a=10 , b=20 , c=30 , d=40)