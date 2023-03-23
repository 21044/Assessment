# imports 'time' to add timing between outputs
import time

amount_correct = 0

# line 5 and 6 creates a list to store the questions and answers respectively
q = ["Which statement do you use to output a message to the screen?", "q2", "q3", "q4", "q5"]
a = ["print", "a2", "a3", "a4", "a5"]

# a function to compare the users inputs and the answers to the questions
def compare(inp, ans):
  if inp == ans:
    time.sleep(0.5)
    print("Correct!")
    global amount_correct
    amount_correct += 1
  else:
    time.sleep(0.5)
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
print('All have no special characters, such as ", (, !, etc')
time.sleep(0.5)
print("Lets begin")
time.sleep(0.5)

# "counter" will go up each time the loop runs through, after "counter" is above the amount of questions it will stop looping
counter = 0
while counter <= len(q) - 1:
  # asks the user a question, each time the loop runs through the number of the list increases which asks a new question
  print(q[counter])
  print("\n")
  time.sleep(0.5)
  user_answer = input("Answer: ").lower()
  if user_answer.isalpha() == False:
    user_answer = input("Please do not use special characters, please try again. ")
  # calls the function "compare()"
  compare(user_answer, a[counter])
  counter += 1

# checks if the amount of correct answers is equal to 5
if amount_correct == 5:
  print("Well done " + name.capitalize() + "! You got them all correct!")
# checks if the amount of correct answers is equal to 0
if amount_correct == 0:
  print("Oh no, you didn't get any correct...")
# checks if the amount of correct answers is within 1 to 4
if amount_correct in range(1,4):
  print("Good job " + name.capitalize() + " you got " + str(amount_correct) + " questions correct!")

print("Thank you for playing!")