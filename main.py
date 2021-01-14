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
  import random
  name_list = ["That's Awesome", "How cool", "I love your name", name + "Is a great name!"]
  print(random.choice(name_list))
  name

if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()