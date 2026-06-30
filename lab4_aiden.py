# Aiden H. | Lab 4 | Intro to Python
# Ticket 1
ages = [17, 11, 25, 13, 9]
for age in ages:
    if age < 13:
        print(f"{age} — Too young ❌")
    else:
        print(f"{age} — Access granted ✅")
# PREDICT: Access granted: 17, 25, 13. Too young: 11, 9.

# EXPLAIN: The variable age holds one age from the list ages at a time as the loop runs.

# Ticket 2
keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("Enter an age: "))
    if age < 13:
        print(f"{age} — Too young ❌")
    else:
        print(f"{age} — Access granted ✅")
    keep_checking = input("Check another age? (yes/no): ")
# PREDICT: If the user types "no" on the first check, the loop runs once because (cont)
# keep_checking is set to "yes" before the loop starts. The loop will end after because "no" was entered

# EXPLAIN: A while loop is the right choice because you don't know how many times (cont)
# the user wants to repeat the loop. The loop keeps running until the user says "no". (cont)
# On the other hand, a for loop runs for a pre-determined time, not up the the user.

# Ticket 3
while True:
    age = input("Enter an age or type 'stop': ")
    if age == "stop":
        break
    age = int(age)

    if age < 13:
        print(f"{age} — Too young ❌")
    else:
        print(f"{age} — Access granted ✅")
# PREDICT: If you forgot the break statement, the loop would never end. (cont)
# Without the break statement, the loop would run and continue asking for (cont)
# another age regardless of the user typing "stop".

# EXPLAIN: The difference is that Ticket 2 uses a control variable (keep_checking), (cont)
# to decide whether the loop continues, while Ticket 3 uses while True and exits the loop (cont)
# once it is told to break by the user typing "stop".

# Ticket 4
def can_access(age):
    if age >= 13:
        return True
    else:
        return False
ages = [17, 11, 25, 13, 9]
for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")
# PREDICT: The output is the same as Ticket 1, but code works differently (cont)
# because the age-checking is now stored inside a function. You don't rewrite the if/else (cont)
# statement every time, the program can call can_access(age) whenever it needs to check an age

# EXPLAIN: Putting the check inside a function is better because you only need to write (cont)
# the age-checking code once and can reuse it whenever you need it by calling can_access(age). (cont)
# This improves code readability and allows for easier updating and fixing

# Ticket 5
def signup_report(ages):
    print("--- StreamPass Signup Report ---")

    approved = 0

    for num, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{num} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{num} | Age {age} — Too young ❌")

    print(f"Approved: {approved} out of {len(ages)}")

signups = [22, 10, 15, 8, 19, 13]

signup_report(signups)
# PREDICT: The output will show each signup number, their age, and whether they (cont)
# got access. Only 4 out of the 6 people will be approved [22, 15, 19, 13].

# EXPLAIN: This function used a function, a parameter, a for loop, enumerate(), (cont)
# if/else statements, and a counter to count how many people get approved.