
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = len(names)
random_number = random.randint(0, x-1)
person = names[random_number]

# person = random.choice(names)

print(person +" is going to buy the meal today!")