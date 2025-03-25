greeting = input("Welcome to love calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter your name: ")
name = name1 + name2  
lower_cased_name = name.lower()
t = lower_cased_name.count("t")
r = lower_cased_name.count("r")
u = lower_cased_name.count("u")
e = lower_cased_name.count("e")
true = t+r+u+e

l = lower_cased_name.count("l")
o = lower_cased_name.count("o")
v = lower_cased_name.count("v")
e = lower_cased_name.count("e")
love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 85:
    print(f"Your score is {love_score}, You go together like coke and mentos")
elif love_score >= 40 and love_score <= 70:
    print(f"Your score is {love_score}, You alright go together")
else:
    print(f"Your score is {love_score}")
