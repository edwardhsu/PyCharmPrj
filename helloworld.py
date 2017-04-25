# Program is to determine whether a person is a boy,
# or a teeanger or a man based on his age.

age = int(input("Please enter your age: "))
if (age <= 12):
    print("You are a kid!")
elif ((age > 12)and(age < 20)):
    print("You are a teenager!")
else:
    print("You are a grown up!")
