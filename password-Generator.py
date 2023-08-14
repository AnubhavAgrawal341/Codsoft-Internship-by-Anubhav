import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic window settings
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 300, 200)

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Create password length input spin box
        self.password_length_label = QLabel("Password length:")
        self.layout.addWidget(self.password_length_label)
        self.password_length_input = QSpinBox()
        self.password_length_input.setRange(1, 128)  # Set range to accept values between 1 and 128
        self.password_length_input.setValue(12)  # Default value
        self.layout.addWidget(self.password_length_input)

        # Create password display
        self.label = QLabel("Generated Password:")
        self.layout.addWidget(self.label)
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.layout.addWidget(self.password_display)

        # Create generate password button
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.central_widget.setLayout(self.layout)

    def generate_password(self):
        # Get length value from the spin box
        password_length = self.password_length_input.value()
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate password of the specified length
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        # Set the password text in the password display
        self.password_display.setText(generated_password)

def main():
    app = QApplication(sys.argv)
    password_generator = PasswordGeneratorApp()
    password_generator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

