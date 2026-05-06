#multiple arguement with input statements

def print_boarding_pass(name,seat):
    print(f" passenger{name}")
    print(f" seat number {seat}")

#need some information
    print("welcome to sacesha's airlines")
#collect data

user_name = input("enter full name")
user_seat = input("please enter seat number")

print_boarding_pass(user_name,user_seat)
