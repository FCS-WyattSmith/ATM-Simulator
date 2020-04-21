'''ATM Simulator
Written by Wyatt Smith 04/20/2020
NOTICE: This program uses the termcolor library and will only run in Repl.it.'''

balance = 1000

def withdrawl(amount):
  global balance
  amount = float(input("How much to withdrawl? "))
  while amount < 0 or amount > (balance - 5):
    if amount < 0:
      amount = float(input("You cannot withdrawl a negative amount. Please enter a different amount. "))
    elif amount > (balance - 5):
      amount = float(input("The account requires at least $5 to remain open. The amount you entered is too high. Please enter a different amount. "))
  balance = round((balance - amount),2)

def deposit(amount):
  global balance
  amount = float(input("How much to deposit? "))
  while amount < 0:
    amount = float(input("You cannot deposit a negative amount. Please enter a different amount. "))
  balance = round((balance + amount),2)

def paybills(type,amount):
  global balance
  print("[1] Electric")
  print("[2] Water")
  print("[3] Gas")
  type = int(input("Which bill to pay? "))
  while not (1 <= type <= 3):
    type = int(input("Invalid bill type. Please enter a valid type. "))
  if type == 1:
    amount = float(input("How much is the electric bill? "))
    while amount < 0 or amount > (balance - 5):
      if amount < 0:  
        amount = float(input("You cannot pay a negative amount. Please enter a different amount. "))
      elif amount > (balance - 5):
        amount = float(input("The account requires at least $5 to remain open. The amount you entered is too high. Please enter a different amount. "))
    balance = round((balance - amount),2)
  elif type == 2:
    amount = float(input("How much for the water bill? "))
    while amount < 0 or amount > (balance - 5):
      if amount < 0:  
        amount = float(input("You cannot pay a negative amount. Please enter a different amount. "))
      elif amount > (balance - 5):
        amount = float(input("The account requires at least $5 to remain open. The amount you entered is too high. Please enter a different amount. "))
    balance = round((balance - amount),2)
  elif type == 3:
    amount = float(input("How much for the gas bill? "))
    while amount < 0 or amount > (balance - 5):
      if amount < 0:  
        amount = float(input("You cannot pay a negative amount. Please enter a different amount. "))
      elif amount > (balance - 5):
        amount = float(input("The account requires at least $5 to remain open. The amount you entered is too high. Please enter a different amount. "))
    balance = round((balance - amount),2)


print("Welcome to ATM Simulator.\n\n")

print("Your account balance is $" + str(balance))
print("[1] Withdrawl")
print("[2] Deposit")
print("[3] Pay Bills")
print("[4] Check Balance")
print("[5] End")
transaction = int(input("Which transaction? "))
while not (1 <= transaction <= 5):
  transaction = int(input("Invalid transaction. Which transaction? "))

while transaction != 5:
  if transaction == 1:
    withdrawl(0.0)
  elif transaction == 2:
    deposit(0.0)
  elif transaction == 3:
    paybills(0,0.0)
  elif transaction == 4:
    print("Your account balance is $" + str(balance))
  print("Your account balance is $" + str(balance))
  print("[1] Withdrawl")
  print("[2] Deposit")
  print("[3] Pay Bills")
  print("[4] Check Balance")
  print("[5] End")
  transaction = int(input("Which transaction? "))
  while not (1 <= transaction <= 5):
    transaction = int(input("Invalid transaction. Which transaction? "))

print("Thank you for using ATM Simulator!")
print("Simulation ended.")
