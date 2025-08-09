my_List = [10, 20, 30, 40, 50]
print(my_List)

print(my_List[0])  # Accessing the first element

print(my_List[1:3])  # Slicing the list

print(my_List[-1])  # Accessing the last element

print(my_List[1:4])  # Slicing the last two elements

my_List.append(60)  # Adding an element to the end
print(my_List)

my_List.remove(20)  # Removing an element
print(my_List)

my_List.pop()
print(my_List)

my_List.pop(1)  # Removing the second element
print(my_List)

my_List = [10, 20, 30, 40, 50]
print(my_List[1:])  # Slicing from the second element to the end

numbers = [1, 2, 3, 4, 5]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)  

print(len(numbers))  # Length of the list

my_List = [10, 20, 30, 40, 50]
my_List.insert(2, 25)  # Inserting 25 at index 2
print(my_List)

my_List = [10, 20, 30, 40, 50]
print(list(reversed(my_List)))


my_List = [10, 20, 30, 40, 50]
my_List.sort(reverse=True)  # Sorting in descending order   
print(my_List)

#Tuple
my_Tuple = (10, 20, 30, 40, 50)
print(my_Tuple)

print(my_Tuple[0])  # Accessing the first element

print(my_Tuple[1:3])  # Slicing the tuple

print(my_Tuple[-1])  # Accessing the last element

print(my_Tuple[1:4])  # Slicing the last two elements

my_Tuple = (10, 20, 30, 40, 50) 
#my_Tuple[3] = 100  # Tuples are immutable, so this will raise an error
print(my_Tuple)

#my_Tuple[3] = 100  # Tuples are immutable, so this will raise an error

my_Tuple = (10, 20, 30, 40, 50)
print(my_Tuple.count(20))  # Counting occurrences of 20

t1 = (1, 2, 3)
t2 = (4, 5, 6)
concatenation = t1 + t2
print(concatenation)  # Concatenating tuples

my_Tuple = (10, 20, 30, 40, 50)
print(20 in my_Tuple)  # Checking if 20 is in the tuple

t = (10,20)
print(t * 3)

my_Tuple = (10, 20, 30, 40, 50)
count = len(my_Tuple)  # Length of the tuple
print(count)

my_Tuple = (10, 20, 30, 40, 20, 50)
print(my_Tuple.index(20))  # Index of the first occurrence of 20


