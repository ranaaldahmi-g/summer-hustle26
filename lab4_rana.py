# Rana Aldahmi | lab 4 | Intro to python

# Ticket 1

ages = [11, 12, 13, 14, 15, 16, 17]

for age in ages:
    if age >= 13:
        print("Access granted!")
    else:
        print("Access denied!")

 # I think ages 11 and 12 will be denied and ages 13, 14, 15, 16, 17 will be granted access  

 # the variable age holds the value of each element in the ages list


 # Ticket 2

    keep_checking = "yes"     
    while keep_checking == "yes":
      age = int(input("Enter your age: "))
      if age >= 13:
        print("Access granted!")
      else:
        print("Access denied!")
      keep_checking = input("Do you want to check another age? (yes/no): ")

# if the user types no, the loop will stop and the program will end. 

# A while loop here is better than a for loop because we dont know how many times the user will want to check an age.


# Ticket 3

while True:
    user_input = input("type 'stop': ")
    if user_input == "stop":
        break
    else:
        print("You did not type 'stop'. Please try again.")
        
# if i forgot the break statement, i predict the program will never end and will keep asking the user to type 'stop'

# the difference between ticket 2's while loop and ticket 3's while loop is that ticket 2's while loop has a condition that can be changed by the user, while ticket 3's while loop will continue until the user types 'stop'


# Ticket 4 

def can_access(age):
    if age >= 13:
        return True
    else:
        return False

ages = [11, 12, 13, 14, 15, 16, 17]
 
for age in ages:
    if can_access(age):
        print(f"Age {age}: Access granted!")
    else:
        print(f"Age {age}: Access denied!")

# The difference between ticket 1 and ticket 4 is that ticket 1 uses a for loop to iterate through the ages list and check each age, while ticket 4 uses a function to check each age. 

# putting the check in every function is better because it makes the code more organized and easier to read.


# Ticket 5

def can_access(age):
    return age >= 13

def signup_report(ages):
    approved_count = 0
    total_signups = len(ages)

print("Streampass signup report")
for signup_num, age in enumerate(ages, start=1):
       if can_access(age):
        status = "Approved"
        approved_count += 1
    else:
        status = "Denied"
        print(f"Signup {signup_num}: Age {age} - {status}")
        print(f"Signups approved: {approved_count}/{total_signups}")

    signups = [11, 12, 13, 14, 15, 16, 17]
    signup_report(signups)

# i think 3 out of 6 will be approved because ages 13, 14, 15, 16, and 17 are all greater than or equal to 13.

# every concept i used to build this lab were for loops, while loops, if statements, functions, and lists. I learned how to use for loops to iterate through a list, how to use while loops to keep asking the user for input until they give a specific answer, how to use if statements to check conditions, how to define and call functions, and how to use lists to store multiple values.