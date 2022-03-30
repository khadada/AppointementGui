# Importing necessary modules and classes
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QWidget, QSpinBox, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Build our class for the program
class BookAppForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
        
    def initialize_ui(self):
        """
        Initialize the window and display its content to the screen.
        """
        self.setGeometry(100, 50, 300,400)
        self.setWindowTitle("4.3 - Appointement Form Gui")
        self.display_widgets()
    
    def display_widgets(self):
        """
        Here we create the necessary widgets for theis application
        """
        