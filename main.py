import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import globals
import shell

globals.globalvars()


class window(QWidget): #Create Window
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = "Iso Editor" + "(" + globals.version + ")"

        self.setMinimumSize(350, 150)

        self.setWindowTitle(title)

        Operations = ["Convert", "Extract", "Combine"]
        global indexint
        indexint = 0

        stringin = Operations[indexint]
        globals.setText(stringin)

        #Drop Down Menu
        global dropdown
        dropdown = QComboBox(self)
        dropdown.move(10, 72)
        dropdown.addItems(Operations)
        dropdown.setCurrentIndex(indexint)

        #Input Textbox
        global textbox
        self.textbox = QLineEdit(self)
        self.textbox.resize(280, 30)
        #self.textbox.resize(self.textbox.sizeHint())
        
        #Convert Button
        global cvtbtn
        cvtbtn = QPushButton(dropdown.currentText() + " File", self)
        cvtbtn.move(0, 100)
        #self.cvtbtn.resize(self.cvtbtn.sizeHint())

        #Output Textbox
        self.textbox2 = QLineEdit(self)
        self.textbox2.resize(280, 30)
        self.textbox2.move(0, 40)
        #self.textbox2.resize(self.textbox2.sizeHint())

        #Select file Button
        selbtn = QPushButton("...", self)
        selbtn.move(285, 0)
        selbtn.setGeometry(285, 5, 50, 30)
        #self.selbtn.resize(self.selbtn.sizeHint())

        selbtn2 = QPushButton("...", self)
        selbtn2.move(285, 0)
        selbtn2.setGeometry(285, 45, 50, 30)
        #self.selbtn2.resize(self.selbtn2.sizeHint())

        dropdown.currentTextChanged.connect(self.onTextChanged)
        #dropdown.currentTextChanged.connect(cvtbtn.setText(globals.operation))
        selbtn.clicked.connect(self.openFileNameDialog)
        selbtn2.clicked.connect(self.saveFileDialog)
        cvtbtn.clicked.connect(self.chooseFile)
        #self.setLayout(vbox)
        self.show()



    def openFileNameDialog(self): #Choose ISO to Convert
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files(*);;Disk Image Files (*.iso);;Wii Backup Image (*.wbfs)", options=options)
        if fileName:
            globals.file = fileName
            self.textbox.setText(fileName)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getSaveFileName()","","All Files(*);;Folder(/);;Disk Image Files (*.iso);;Wii Backup Image (*.wbfs)", options=options)
        if fileName:
            globals.cvfile = fileName
            self.textbox2.setText(fileName)
    
    def chooseFile(self):
        globals.storeFile(self.textbox.text())
        globals.convertFileName(self.textbox2.text())
        shell.main()

    def onTextChanged(self):
        if (dropdown.currentIndex() == 2):
            window.getCombineSave(self)

        operate = dropdown.currentText()
        globals.setText(operate)
        cvtbtn.setText(globals.operation + " File")
        print (str(dropdown.currentIndex()))

    def getCombineSave(self):
        global destination 
        text, destination = QInputDialog.getText(self, "Save Name", "Name of Combined Iso: ")
        if destination:
            if (text == ""):
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("You didn't input any text!")
                msg.exec_()
                window.getCombineSave(self)
            globals.CombineFileName(text)
        else:
            dropdown.setCurrentIndex(indexint)

def main(): #Main Loop

    application = QApplication(sys.argv)
    app = window()
    sys.exit(application.exec_())



if __name__ == '__main__':
    main()