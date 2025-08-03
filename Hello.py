print("Welcome to, Python!")

# Arithmetic Operator
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print()  # Adds a blank line

# Comparison operator
print(a == b)  # equal to
print(a != b)  # not equal to
print(a < b)   # Less than
print(a > b)   # Greater than
print()  # Adds a blank line

# Logical operator 
print(a > 0 and b > 0)  # Logical AND
print(a > 0 or b < 0)   # Logical OR 
print(not (a > b))
print()

#Data types
name = "John Doe"
age = 30
is_student = True
height = 5.9
print(name,age,is_student,height)
print()


#concatination
text = "Handle"
print(text + " Carefully")
print(text * 5)
print(text[0:3])
print(text.lower())
print(text.upper())
print()

text = "Python"
print(text[-6:-2]) #Negative indexing
print()
print(text[0:4]) #positive indexing 
print()
print(text[2:5]) #Slicing with step
print()
print(text[-4:-1])