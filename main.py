# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Each of the 3 figures below total 90 years
totaldays = 32850
totalweeks = 4680
totalmonths = 1080

#calculate age so far in d/m/y
daysused = int(age) * 365
daysleft = totaldays - daysused

weeksused = int(age) * 52
weeksleft = totalweeks - weeksused

monthsused = int(age) * 12
monthsleft = totalmonths - monthsused


print(f"You have {daysleft} days, {weeksleft} weeks or {monthsleft} months left. Use them wisely")

