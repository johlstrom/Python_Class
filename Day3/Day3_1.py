# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remainder_check = number % 2

if remainder_check == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")