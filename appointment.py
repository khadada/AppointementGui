# Importing necessary modules and classes
import sys
from tkinter import Label, Spinbox
from turtle import title
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QWidget, QSpinBox, QHBoxLayout, QVBoxLayout, QComboBox,QLineEdit, QTextEdit,QMessageBox, QFormLayout)
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
        # Create Widgets
        # 1 - Header title
        title = QLabel("Appointement Submission Form")
        title.setFont(QFont("Tahoma",20))
        title.setAlignment(Qt.AlignCenter)
        # 2 - name & address & mobile & age etc ...
        name = QLineEdit()
        name.resize(150, 60)
        
        address = QLineEdit()
        address.resize(150, 60)
        
        mobile = QLineEdit()
        mobile.resize(150, 60)
        mobile.setInputMask("00_00_00_00_00")
        
        age_lbl = QLabel('Age:')
        age = QSpinBox()
        age.setRange(10, 90)
        
        height_lbl = QLabel("Height:")
        height = QLineEdit()
        height.setPlaceholderText(" Cm ")
        
        weight_lbl = QLabel("Weight:")
        weight = QLineEdit()
        weight.setPlaceholderText(" Cm ")
        
        gender = QComboBox()
        gender.addItems(["Male","Femal"])
        
        surgery = QTextEdit()
        surgery.setPlaceholderText("Seperate by ','")
        
        blood_type = QComboBox()
        blood_type.addItems(["A+","B+","AB+","O+","A-","B-","AB-","O-"])
        
        hours = QSpinBox()
        hours.setRange(1, 12)
        
        minuts = QSpinBox()
        minuts.setRange(0, 59)
        
        am_pm = QComboBox()
        am_pm.addItems(["AM","PM"])
        
        submit_btn = QPushButton("Book Appointment")
        submit_btn.clicked.connect(self.set_appointment)
        
        # 3- Create Horizontal Layout:
        h_box = QHBoxLayout()
        h_box.addSpacing(10)
        h_box.addWidget(age_lbl)
        h_box.addWidget(age)
        h_box.addWidget(height_lbl)
        h_box.addWidget(height)
        h_box.addWidget(weight_lbl)
        h_box.addWidget(weight)
        
        # Create Horizontal layout for the time:
        time_h_box = QHBoxLayout()
        time_h_box.addSpacing(10)
        time_h_box.addWidget(hours)
        time_h_box.addWidget(minuts)
        time_h_box.addWidget(am_pm)
        
        # Create Form Layout:
        app_form_layout = QFormLayout()
        
        # Add All widgets to Form Layout:
        app_form_layout.addRow(title)
        app_form_layout.addRow("Full Name",name)
        app_form_layout.addRow("Address:", address)
        app_form_layout.addRow("Mobile n°:", mobile)
        app_form_layout.addRow(h_box)
        app_form_layout.addRow("Gender:",gender)
        app_form_layout.addRow("Past Sugeries:",surgery)
        app_form_layout.addRow("Blood Type",blood_type)
        app_form_layout.addRow("time",time_h_box)
        app_form_layout.addRow(submit_btn)
        
        # Set Layout For app
        self.setLayout(app_form_layout)
 
    def set_appointment(self):
        """
        Show message for success create appoitment and close app
        """
        QMessageBox.information(self,"Success Create Appointment","All Done with sucessfully",QMessageBox.Ok,QMessageBox.Ok)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookAppForm()
    sys.exit(app.exec_())