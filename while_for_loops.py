is_learning = True

while is_learning:
    user_input = input("Are you still learning?(yes/no) ")
    is_learning = user_input == "yes"
    print(user_input)

 #while loop yes or no example
  
  
user_input = input("Are you still learning?(yes/no) ")
while user_input == "yes":
   print("we are running!")
   user_input = input("Are you still learning?(yes/no)")
print("stopped")   