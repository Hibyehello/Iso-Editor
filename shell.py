import subprocess
import globals

def main():
    print(globals.infile)
    print(globals.cvinFile)
    operate = globals.operation
    
    if (globals.operation == "Convert"):
        subprocess.call(["wit", "copy", globals.infile, globals.cvinFile])
    elif (globals.operation == "Extract"):
        subprocess.call(["wit", "extract", globals.infile, globals.cvinFile])



