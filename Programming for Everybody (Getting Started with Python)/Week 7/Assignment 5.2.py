# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters 
# anything other than a valid number catch it with a try/except and put out an appropriate message and 
# ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None 
smallest = None 

while True:
    num = input("Enter a number: ")
    if num == "done":
        break 
           
    try: 
        num1 = int(num) 
    
    except: 
        print("Invalid input") 
        continue 
        
    if largest is None or num1 > largest:
        largest = num1 
    
    if smallest is None or num1 < smallest:
        smallest = num1 

print("Maximum is", largest) 
print("Minimum is", smallest)





# It would be much easier


li = list()

while True:
    num = input("Enter a number: ")
    if num == "done":
        break 
           
    try: 
        num1 = int(num)
        li.append(num1)
        
    except: 
        print("Invalid input") 
        continue 

li1=sorted(li)

print("Maximum is", li1[-1]) 
print("Minimum is", li1[0])