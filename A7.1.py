#Assignment 7.1
#Tristan Werden
#TODO: None
#NOTES: I added a try/except that isn't on the flowchart, but only because I kept miss-typing the file name and felt stupid.

userin = input("Enter file name: ")
print(userin)

try :
    fin = open(userin)
except :
    print("Failed to open file - how hard is it to enter a valid input?")
    quit()

for line in fin :
    print(line.upper().strip())
