def globalvars():
    global version
    global file
    global cvfile

# Define Global Variables
    version = "v1"
    file = ""
    cvfile = ""

def storeFile(inString):
    global infile
    infile = inString
    #print (infile)

def convertFileName(inString):
    global cvinFile
    cvinFile = inString


def setText(inString):
    global operation    
    operation = inString

def CombineFileName(inString):
    global destination
    destination = inString
    print (destination)
    print(inString)