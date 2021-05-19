from random import randrange
def main():
  name = input("What is your name? ")
  age = int(input("What is your age?"))

  personal_name(name)
  space()
  name_len(name)
  space()
  drivers_age(age)
  space()
  lucky_number()
  


def personal_name(name):
  print("Welcome,",name)

def name_len(name):
  length=len(name)
  print("Your name is",length,"Charachters long")

def drivers_age(age):
  if age >=16:
    print("You are able to drive")
  else:
    print("You are not able to drive")  

def lucky_number():
  number = randrange(1,100,1)
  print("Your Lucky Number is:",number)

def space():
  print("---------------------------")

main()
