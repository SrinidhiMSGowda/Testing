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
print(text[2:5]) #Slicing with step positive
print()
print(text[-4:-1]) #Negative slicing 
print()

#conditional statement
age = int(input("Enter your age: "))
if age > 18:
    print("You are a Adult")
elif age >= 13:
    print("You are a Teenager")
else:
    print("You are a Child")

#Loop 
for i in range(1, 5):
    print(i)
    print()

#while loop
count = 1
while count <= 3:
    print(count)
    count += 1  
    print()

#Nested Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        print()
import random

number = random.randint(1, 100)
attepts = 0

print ("Welcome to the Guess the Number Game!")

while True:
    guess = int(input("Enter your guess: "))
    attepts += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attepts} attempts.")
        break