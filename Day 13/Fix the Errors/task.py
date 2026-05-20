try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have entered an invalid input type. Kindly enter numerical value such as 10")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
