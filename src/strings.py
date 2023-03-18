fact = "The Moon has no atmosphere."
fact += " No sound can be heard on the Moon."
print(fact)

# We can use triple quotation marks when the string uses both single and double quotation marks
another_fact = """We only see about 60% of the Moon's surface, this is known as the "near side"."""
print(another_fact)

# Triple quotation marks can also help us with multiline text
multiline_text = """Facts about the Moon:
- There is no atmosphere.
- There is no sound."""
print(multiline_text)
# ... or you can use tne newline character \n
multiline_with_newline_char = "Facts about the Moon:\n- There is no atmosphere.\n- There is no sound."
print(multiline_with_newline_char)

# Title
print("----- Title -----")
heading = "temperatures and facts about the moon"
heading.title()
print(heading)

# Split
print("----- Split -----")
temperatures = """Daylight: 260F
Nighttime: -280F
"""
# With no arguments, the split automatically separate the string at every space
print(temperatures.split())
# With a string as an argument, the method will look for it in the string and separate it right there
print(temperatures.split("\n"))

# Join
# This method receives an iterable list as an argument
print("----- Join -----")
moon_facts = ["The moon is drifting away from the Earth.", "On average, it is moving away 4cm yearly"]
print("\n".join(moon_facts))
new_string = "PIZZA".join(moon_facts)
print(new_string)


# Search
print("----- Search -----")
Moon = "This is the natural satellite of earth"
if "satellite" in Moon:
    print("The word satellite is in the Moon variable")
if "star" not in Moon:
    print("The word Star is not in the Moon variable")

# Find
print("----- Find -----")
temperatures = """Saturn has a daytime temperature 
of -170 degrees Celsius, while Mars has
-28 Celsius."""
# This method returns the index on which the given string is first found
# it is case sensitive, and will return -1 if the character was not found
print(temperatures.find("t"))
print(temperatures.find("T"))
print(temperatures.find(" "))
print(temperatures.find("-170"))
print(temperatures.find("\n"))

# Count
# it will return 0 in case there is no match
print("----- Count -----")
random_string = "Hello world this is just a test!!"
print(random_string.count("Hello"))
print(random_string.count("!"))
print(random_string.count("!!"))
print(random_string.count("Bye"))

# Lower and upper
print("----- Lower and upper -----")
name = "Carlos"
print(name.lower())
print(name.upper())

# Check content
print("----- Check content -----")
random_string = "Mars average temperature is: -60C"
parts = random_string.split(':')
# -1 returns the last element of the array
# Negative numbers start counting from the end
print(parts[-1])

# Complex check
print("----- Complex check -----")
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

# Starts with
print("----- Starts and Ends with -----")
print("-60".startswith("-"))
print("30C".endswith("C"))

# Replace
# The first argument is the term to look for and the second one is the new term
print("----- Replace -----")
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius".replace("Celsius", "C"))