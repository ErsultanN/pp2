# Ex1
carname = "Volvo"
print(carname)

# Ex2
x = 50
print(x)

# Ex3
x = 5
y = 10
print(x + y)

# Ex4
x = 5
y = 10
z = x + y
print(z)

# Ex5
x,y,z = "Orange", "Banana", "Cherry"
print(x,y,z)

# Ex6
x = y = z = "Orange"
print(x,y,z)

# Ex7
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    print(x)
    
    myfunc()