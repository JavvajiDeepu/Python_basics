friend = "rolf"
f1= "sai"
user_name = input("enter your name:" )
# if is not true it jumps to elseif
if user_name == friend:
    print("hello, friend!")
#  elseif is not true it jumps to else 
elif user_name == f1:
    print("hello")
else:
    print("hii")    

# if with bool statements

Name = input("enter your naame: ")
print(bool(Name))
if Name:
    print("we know your name.")

