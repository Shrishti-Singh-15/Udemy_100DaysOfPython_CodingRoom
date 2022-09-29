# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
remaining = 90 - age_int
months = remaining * 12
weeks = remaining * 52
days = remaining * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")



