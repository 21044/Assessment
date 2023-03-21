# imports 'time' to add timing between outputs
import time

# line 5 and 6 creates a list to store the questions and answers respectively
q = ["q1", "q2", "q3", "q4", "q5"] #q1, etc, are placeholders
a = ["a1", "a2", "a3", "a4", "a5"] #a1, etc, are placeholders

amount_correct = 0 

# a function to compare the users inputs and the answers to the questions
def compare(inp, ans):
  if inp == ans:
    print("Correct!")
    amount_correct + 1
  else:
    print("Wrong")

print("Hey there!")
# "time.sleep()" will make the program wait before doing the next step
time.sleep(0.5)
print("Welcome to my quiz.")
time.sleep(1)
# asks the user for their name and will store it in a variable
name = input("What is your name? ")
# makes a loop which will only run when the variable "name" has any numbers or symbols in it
while name.isalpha() == False:
  name = input("That is an invalid name, Please enter a proper name. ")
# after the loop ends the program will use the variable in a string
time.sleep(0.5)
print("Hello " + name.capitalize())
print("I will begin to ask you some questions about ")

# "counter" will go up each time the loop runs through, after "counter" is above 4 it will stop looping
counter = 0
while counter <= 4:
  # asks the user a question, each time the loop runs through the number of the list increases which asks a new question
  print(q[counter])
  user_answer = input("Please Input Your Answer: ")
  # calls the function "compare()"
  compare(user_answer, a[counter])
  counter += 1

if amount_correct == 5:
  print("Well done, you got them all correct!")
if amount_correct == 0:
  print("Oh no, you didn't get any correct...")
else:
  print("Good job, you got " + amount_correct + " Correct")