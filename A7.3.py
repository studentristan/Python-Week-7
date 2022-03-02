#Assignment 7.3
#Tristan Werden
#TODO: None
#NOTES: I added a try/except that isn't on the flowchart, but only because I kept miss-typing the file name and felt stupid.

userin = input("Enter file name: ")

def properrun():

    count = 0
    total = 0

    try:
        fin = open(userin)
    except:
        print("File cannot be opened")
        quit()

    for line in fin:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        count = count+1
        total = total + (float(line[line.find('0'):])) #being able to steal this line from last week was awesome!
        #print(count)
        #print(total)
    print("Average spam confidence:", total/count)

if userin == "na na boo boo":
    print("You have been punk'd!!!!!!!!!")
else:
    properrun()
