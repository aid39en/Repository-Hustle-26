# Aiden Huynh|Lab 3|Blue

# Ticket 1
username = "aid39en" # PREDICT: this has 7 characters.
print(len(username))
# len(username) did in fact count every character, total of 7.

# Ticket 2
print(username[0]) # PREDICT: pushes out "a"
print(username[len(username)-1]) # PREDICT: pushes out "n"
# The last index is len(username) - 1 because Python indexes begin counting at 0, (cont)
# therefore the last character should be one position before the total length as measuring lengths begin at 1.

# Ticket 3 
print("Welcome to Loop, @" + username + "!") # username is the variable containing my username.
print(f"Welcome to Loop, @{username}!") # PREDICT: Both versions should print "Welcome to Loop, @aid39en!"
# Concatenation felt easier as I can process the text in a logical way, (cont)
# adding each piece of text together step by step to create the intended output.

# Ticket 4
# username[0] = "X" # run this, it breaks on purpose.
# PREDICT: Before running the broken line, I thought the first character of the username would change to X.
# TypeError: 'str' object does not support item assignment
print(username.upper()) # the right way
# Immutable strings mean their individual characters cannot be changed after the string is created.

# Ticket 5
feed = [
    "Finished my homework!",
    "Great day at school!",
    "Hanging out with my friends!"
]

print(len(feed)) # PREDICT: The count will be 3, and "Finished my homework!" will print first.
print(feed[0]) # PREDICT: "Finished my homework!" will print first.
# I used print(feed[0]) to get the first post because Python lists start counting at 0.

# Ticket 6
feed.append("Only 5 more minutes until school ends!") # PREDICT: The fourth post will have an index of 3
print(feed)
# The fourth post sits at index 3 because Python lists start counting from 0 resulting in that number .

# Ticket 7

feed.pop(0)    # removes the first post.
feed.sort()    # puts the remaining posts in alphabetical order.

print(feed)

# PREDICT: "Finished my homework!" will be removed.
# The remaining posts will be sorted alphabetically.

# I used .pop(0) to remove the first item in the list.
# Then, I used .sort() to arrange the remaining posts in alphabetical order.

# Ticket 8

profile = {
    "username": "aid39en",
    "followers": 100,
    "verified": False
}

print(profile["followers"])

# PREDICT: The follower number printed will be 100.
# profile[0] will cause an error because dictionaries do not use number indexes.

# profile[0] # run this, it breaks on purpose.
# KeyError: 0

# Dictionaries use key names instead of number indexes because each value is
# stored using a label, making it easier to find specific information compared to 
# lists relying on a position number.

# Ticket 9

profile["followers"] = profile["followers"] + 50
profile["bio"] = "Learning Python and coding!"

print(profile)
# print(profile.get("age"))

# PREDICT: .get("age") will print None because the key does not exist.

# .get() is safer because it returns None instead of causing an error when the key is missing.

# Ticket 10

print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")

# PREDICT: @aid39en has 150 followers and 3 posts. Top post: Great day at school!

# I used a dictionary (profile) to get the username and follower count,
# and a list (feed) to get the post count and first post.
