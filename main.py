"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util
import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")
  print("My name is Chat Bot")
  name = input("What's your name?: ")
  name_list = ["That's Awesome", "How cool", "I love your name", name + " is a great name!"]
  print(random.choice(name_list))
  wyd = input("What are you doing?:")
  wyd
  wyd_list = ["Oh ok", "cool", "Nice"]
  print(random.choice(wyd_list))
  color = input("What's your favorite color? ")
  color
  color_list = ["that's awesome", "Mine too", "Oh wow", "cool" ]
  print(random.choice(color_list))
  grade = int(input("What grade are you in?(1-12)(N/A):"))
  if  grade <= 5: 
    print("You're in Elementary School. That's Awesome!")
  elif grade > 5 and grade <= 8:
    print("You're in Middle School. That's Awesome!")
  elif grade > 8 and grade <= 9: 
    print("You're in High School. That's Awesome!")
  else:
    print("You're not in school. That's Awesome!")
  subject = input("What's your favorite subject? ")
  if subject == "Math":
    print("cool")
  elif subject == "Science":
    print("no way")
  elif subject == "ELA" or subject == "English":
    print("how cool")
  elif subject == "Social Studies" or subject == "History":
    print("Mine too")
  else:
    print("so cool")
  food = input("Are you hungry?: ")
  if food == "yes" or food == "y" or food == "Yes" or food == "Y":
    print("You should grab a snack")
  elif food == "No" or food == "n" or food == "no" or food == "N":
    print("That's good")
  else: 
    print("Oh ok")
  a = input("I had a nice time talking to you! Did you enjoy our conversation?: ")
  if a == "yes" or a == "Yes" or a == "y" or a == "Y":
    print("I'm glad you enjoyed our conversation")
  elif a == "no" or a == "No" or a == "n" or a == "N":
    print("I'm sorry to hear that I hope you enjoy our next conversation better.")
  else: 
    print("Oh ok")

  goodbye = ["Have a good day", "goodbye", "Talk to you soon"] 
  random.choice(goodbye)  


if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()