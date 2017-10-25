# for i in [0, 1, 2, 3]:
#     print i

# supplies = ["pens", "staplers", "flame-throwers", "binders"]
#
# for i in range(len(supplies)):
#     print("Index " + str(i) + ' in supplies is: ' + supplies[i])

myPets = ["zophie", "pooka", "fat-tail"]
print("Enter a pet name: ")
name = input()
if name not in myPets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")
