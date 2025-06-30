print("Welcome to my quiz game about programming!")
score = 0
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! :)")

answer = input("What does HTML stand for? ")
if answer.lower() == "HyperText Markup Language":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'hypertext markup language'.")

answer = input("What is the output of 2**3? in python? ")
if answer.lower() == "8":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is '8'.")

answer = input("Which data type would you use to store a list of items in Python? ")
if answer.lower() == "list":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'list'.")   

answer = input("Which data type would you use to store True or False? ")
if answer.lower() == "boolean":  
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'boolean'.")

answer = input("Which data structures follows the Last In First Out (LIFO) principle? ")
if answer.lower() == "stack":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'stack'.")

answer = input("Which built in python data structures is used to check if an item exists in a collection? ")
if answer.lower() == "set":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'set'.")

answer = input("Which principle of OOP allows you to create new classes based on existing ones? ")
if answer.lower() == "inheritance":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'inheritance'.")

answer = input("Which data structure is used to store key-value pairs in Python? ")
if answer.lower() == "dictionary":
    print("Correct!")
    score += 1  
else:
    print("Incorrect! The correct answer is 'dictionary'.") 

answer = input("Which data structure is best for implementing undo feature in a text editor? ")
if answer.lower() == "stack":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'stack'.")

answer = input("Which data structure is used to implement a priority queue? ")
if answer.lower() == "heap":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'heap'.")   

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
print("Thanks for playing!")
