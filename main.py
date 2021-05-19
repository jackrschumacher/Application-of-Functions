
def main():
  name = input("What is your name? ")
  age = int(input("What is your age?"))

  personal_name(name)
  name_len(name)
  drivers_age(age)


def personal_name(name):
  print("Welcome,",name)

def name_len(name):
  length=len(name)
  
def drivers_age(age):
  if age >=16:
    print("You are able to drive")
  else:
    print("You are not able to drive")  



main()
