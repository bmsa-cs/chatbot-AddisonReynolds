"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util
import random

def run_tests():
  """This function will check for the pytest module"""
  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")
  print("My name is Chat Bot and my friends call me Fiona!")
  name = input("What's your name?: ")
  name_list = ["That's Awesome", "How cool", "I love your name", name + " is a great name!"]
  print(random.choice(name_list))
  wyd = input("What are you doing?:")
  wyd
  wyd_list = ["Oh ok", "cool", "Nice"]
  print(random.choice(wyd_list))
  color = input("What's your favorite color?")
  color
  color_list = ["that's awesome", "Mine too", "Oh wow", "cool" ]
  print(random.choice(color_list))
  grade = int(input("What grade are you in?(1-12):"))
  grade 
  if  grade <= 5: 
    print("You're in Elementary School. That's Awesome!")
  elif grade > 5 and grade <= 8:
    print("You're in Middle School. That's Awesome!")
  elif grade > 8 and grade <= 9: 
    print("You're in High School. That's Awesome!")
  else:
    print("You're not in school. That's Awesome!")
    

if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()