x = 97
y = 55
# test expression
if x > y:
    # statement to be run
    print(y)

a = 93
b = 27
if a < b:
    print("A less than B")
    print("Hello world")
else:
    print("B greater than A")

# indentation is key to nest conditions 
i = 24
j = 44
if i <= 0:
    print(i)
    print(j)
    if(i < j):
        print ("i less than j")

# Use of else if
aa = 93
bb = 93
if aa > bb:
    print("aa is greater than bb")
elif aa < bb:
    print("aa is less than bb")
else: 
    print ("aa is equal to bb")    

#nested if, else, elif
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

#or
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

x = 23
y = 34
if x != 34 and y == 34:
    print(x + y)