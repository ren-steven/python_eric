
# This is for looping over one list
Letters = ["abc","defgh","cdef","efghij"]
for letter in Letters:
    if len(letter)>= 5:
        print("this is a long word: " + letter)
    elif len(letter)< 5:
        print("this is a short word: " + letter)



# This is to loop over one list (again)
letters = ["abc","def","ghi","jkl"]
index = 0
for each in letters:
    print(letters[index])
    index = index + 1

print("The value of index is: " + str(index))
index = 3    
for each in letters:
    print("The value of index is: " + str(index))
    print(letters[index])
    index = index - 1


# This is to loop over two lists
animals = ["sheep","horse","cow"]
colors = ["black","red","white"]
index = 0
index2 = 2
for each in animals:
    print(colors[index]+ " " + animals[index])
    index2 = index2 - 1
    index = index + 1



# This is to practice the "while loop"
#When it says 'Throw a ballon y/n, you press y to go to splash and ask for another ballon or n to exit :D
answer = input("Throw a water ballon? (y/n)")
while answer == "y":
    print("Splash!!!!!!!")
    answer = input("Throw another water ballon? (y/n)")
print("He's so wet!!!!!!!!!!!!!!!!!!!!")



# This is to practice the infinite loop
# P.S -> BE CAREFUL!!!!!!!!!!!!!!!!!!!!!!!!
# P.S.S -> use ctrl-c to stop loop
count = 5
while True:
    print("This is an infinite loop!"+ "count =" + str(count))
    if count == 200:
        break
    count = count + 195



