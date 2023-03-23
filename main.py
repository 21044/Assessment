# imports 'time' to add timing between outputs
import time

amount_correct = 0

# line 5 and 6 creates a list to store the questions and answers respectively
q = ["q1", "q2", "q3", "q4", "q5"] #q1, etc, are placeholders
a = ["a1", "a2", "a3", "a4", "a5"] #a1, etc, are placeholders

# a function to compare the users inputs and the answers to the questions
def compare(inp, ans):
  if inp == ans:
    print("Correct!")
    global amount_correct
    amount_correct += 1
  else:
    print("Wrong")
    

print("Hey there!")
# "time.sleep()" will make the program wait before doing the next step
time.sleep(0.5)
print("Welcome to my quiz.")
print("\n")
time.sleep(1)
# asks the user for their name and will store it in a variable
name = input("What is your name? ")

# makes a loop which will only run when the variable "name" has any numbers or symbols in it
while name.isalpha() == False:
  name = input("That is an invalid name, Please enter a proper name. ")
# after the loop ends the program will use the variable in a string
time.sleep(0.5)
print("Hello " + name.capitalize())
time.sleep(0.5)
print("\n")
print("I am going to ask you some questions about Python")
time.sleep(0.5)
print("Lets begin")
time.sleep(0.5)

# "counter" will go up each time the loop runs through, after "counter" is above the amount of questions it will stop looping
counter = 0
while counter <= len(q) - 1:
  # asks the user a question, each time the loop runs through the number of the list increases which asks a new question
  print(q[counter])
  print("\n")
  user_answer = input("Answer: ")
  # calls the function "compare()"
  compare(user_answer, a[counter])
  counter += 1

if amount_correct == 5:
  print("Well done " + name.capitalize() + "! You got them all correct!")
if amount_correct == 0:
  print("Oh no, you didn't get any correct...")
if amount_correct in range(1,4):
  print("Good job " + name.capitalize() + " you got " + str(amount_correct) + " questions correct!")