import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Create the central widget for the application
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create the layout for the central widget
        self.layout = QGridLayout()

        # Create a display widget to show the entered numbers and calculations
        self.display = QLineEdit()
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        # Call the function to create the calculator buttons
        self.create_buttons()

        # Set the layout for the central widget
        self.central_widget.setLayout(self.layout)

        # Variable to store the current value entered by the user
        self.current_value = ""

    def create_buttons(self):
        # Define the buttons and their positions in the grid layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        # Create buttons for each entry in the buttons list and connect the click event to on_button_click function
        for btn_text, row, col in buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(lambda checked, text=btn_text: self.on_button_click(text))
            self.layout.addWidget(button, row, col)

    def on_button_click(self, text):
        if text == "=":
            try:
                # Evaluate the current expression and display the result
                result = eval(self.current_value)
                self.display.setText(str(result))
                self.current_value = str(result)
            except Exception as e:
                # Display an error message if the expression is invalid
                self.display.setText("Error")
                self.current_value = ""
        else:
            # Append the clicked button's text to the current value
            self.current_value += text
            self.display.setText(self.current_value)

def main():
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
