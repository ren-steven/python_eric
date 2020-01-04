# This is for the "print" function
print("This is a parameter")


# This is for the "input" function
#name = input("What is your name?")
#print (name)


# This is for the "count" function
count = "functions are fun".count("fun")
print(count)


# This is for the function "upper"
letter_upper = "blue".upper()
print(letter_upper)


# This is for the function "reverse"
countdown = [1, 2, 3,]
countdown.reverse()
print(countdown)


# This is an example for the function "reverse"
animals = ["sheep","horse","cow"]
colors = ["black","red","white"]
index = 0
animals.reverse()
for each in animals:
    print(colors[index] +" "+ animals[index])
    index = index + 1


# This is for the "replace" function
message = "Coding makes me happy!"
message2 = message.replace("happy",":D")
print(message)
print(message2)


# Making the function "ice_cream"
def ice_cream():
    print("ice_cream")
    print("chocolate")
    print("strawberry")
    print("vanila")

ice_cream()


# Making ice_cream more complex
def ice_cream(flavour):
    print(flavour +" "+ str(len(flavour)))


ice_cream("vanila")
ice_cream("chocolate")
    
