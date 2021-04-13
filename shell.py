import subprocess

from PyQt5.QtWidgets import QInputDialog
import globals

def main():
    print(globals.infile)
    print(globals.cvinFile)
    operate = globals.operation
    
    if (globals.operation == "Convert"):
        subprocess.call(["wit", "copy", globals.infile, globals.cvinFile])
    elif (globals.operation == "Extract"):
        subprocess.call(["wit", "extract", globals.infile, globals.cvinFile])
    elif (globals.operation == "Combine"):
        subprocess.call(["wit", "mix", globals.infile, globals.cvinFile, "--dest" , globals.destination + ".iso"])



