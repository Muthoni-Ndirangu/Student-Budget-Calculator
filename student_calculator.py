def welcome ():
  print("====================")
  print("Welcome to our student calculator!")
  print("====================")
welcome()
while True:
 try:
   money = int(input("Enter your pocket money"))
   if money <= 0:
     print("Enter an amount greater than zero:")
   else:
    break
 except ValueError:
    print("Invalid input")
food = int(input("Enter amount spent on food"))
while food < 0:
  print("Enter a valid amount")
  food = int(input("Enter the amount spent on food")) 

shopping = int(input("enter the shopping expenses:"))
while shopping < 0:
  print("Enter a valid ammount")
  shopping = int(input("Enter the shopping expenses"))

transport = int(input("Enter the transport expenses"))
while transport < 0:
  print("enter a valid amount")
  transport = int(input("Enter the transport expenses"))
other = int(input("enter other expenses"))
while other < 0:
  print("Enter a valid amount")
  other = int(input("enter other expenses"))
expenses = food + transport + shopping + other 
print("Your total expenses are:", expenses) 
balance = money - expenses
if money > 0 and expenses >= money * 0.8:
  print("Warning! You have spent 80%or more of your pocket money!:")
print("Your total expenses were:", expenses)
if balance > 0:
  print("You have money left")
  print("The amount of money left is:", balance)
elif balance == 0:
  print("You have spent all your money.")
else:
  print("You have over spent your money.")
  print("You are short by: ", abs(balance))
if money > 0:
  percentage = (expenses / money) * 100
  print("The percentage of money you spent:", round(percentage,2), "%")
if percentage < 50:
  print("Good spending habbits")
elif percentage < 80:
  print("Be careful with your spending")
else:
  print("Overspending alert")
if balance > 0:
    savings = balance
    savings_percentage = (savings / money) *100
    print("Your potential savings are:", savings)
    print("Your saving percentage is:", round(savings_percentage, 2),"%")
else:
    print("You have no money available for saving")
    
    


        


        
  