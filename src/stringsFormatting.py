# percentage sign
# It works sort of like a pointer. You can pass the variables to print at the end of the sentence
# %s is for strings
print("----- String interpolation -----")
mass_percentage = "1/6"
print("On the moon you would weight about %s of your weight on earth" % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# %f is for float
print("Mr. %s, the total is %.2f." % ("Jekyll", 15.53))

#Format method
#Same than %
print("----- Format method -----")
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#F Strings
print("----- F Strings -----")
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

#HOLD THE FUCK UP
hola = "Hola mundo"
f"{hola}"
print(f"{hola}")