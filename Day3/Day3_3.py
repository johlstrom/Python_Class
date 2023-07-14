# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

year_test4 = year % 4
year_test100 = year % 100
year_test400 = year % 400

if year_test4 == 0:
    if year_test100 == 0:
        if year_test400 == 0:
            print("Leap Year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")