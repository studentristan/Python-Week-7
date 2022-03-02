#Assignment 7.2
#Tristan Werden
#TODO: None
#NOTES:

userin = input("Enter file name: ")

try :
    fin = open(userin)
except :
    print("Failed to open file - how hard is it to enter a valid input?")
    quit()

count = 0
total = 0

for line in fin:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    total = total + (float(line[line.find('0'):])) #being able to steal this line from last week was awesome!
    #print(count)
    #print(total)
print("Average spam confidence:", total/count)
