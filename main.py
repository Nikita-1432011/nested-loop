string = input("Plz enter your word:")

char = input("plz enter your character which you want to know the result:")

i=0
count=0

while(i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1

print("The total number of times",char,"has occured = ",count )