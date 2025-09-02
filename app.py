import sys

# Import af filen/modulet roeversprog.py -
import roeversprog

from PySide6.QtWidgets import QApplication 
from PySide6.QtUiTools import QUiLoader
# Læg mærke tile at QMainWindow ikke importeres.
# I stedet importeres QObject i stedet for.
# QMainWindow er anvendt i Designer.
from PySide6.QtCore import QObject


loader = QUiLoader()


class Roeversprogsoversaetter(QObject):
    def __init__(self):
        super().__init__()
        # Her loades brugerfladen fra Designer.
        self.ui = loader.load("roeversprogsoversaetter.ui", None)
        self.ui.oversaet_knap.clicked.connect(self.oversaet)
        self.ui.reverseButton.clicked.connect(self.reverse)
        self.reversedState = False

    def oversaet(self):
        # Denne metode anvender funktionen oversaet_til_roeversprog, som
        # ligger i modulet roeversprog (som er importeret i starten)
        if self.reversedState == False:
            output = roeversprog.oversaet_til_roeversprog(self.ui.inputBox.toPlainText())
        else:
            output = roeversprog.oversaet_fra_roeversprog(self.ui.inputBox.toPlainText())
        # Set the output box to show the translated text.
        self.ui.outputBox.setPlainText(output)

    def reverse(self):
        """ Reverse the translation. """
        self.reversedState = not self.reversedState
        self.ui.inputBox.setPlainText("")
        self.ui.outputBox.setPlainText("")
        if self.reversedState == True:
            self.ui.inputLabel.setText("Røversprog")
            self.ui.outputLabel.setText("Regular language")
        else:
            self.ui.outputLabel.setText("Røversprog")
            self.ui.inputLabel.setText("Regular language")


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
roeversprogsoversaetter = Roeversprogsoversaetter()
roeversprogsoversaetter.ui.show()
program.exec()
