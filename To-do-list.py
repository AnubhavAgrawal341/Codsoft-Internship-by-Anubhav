import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QDialog

# This class is a dialog that will pop up when an existing task is edited
class EditTaskDialog(QDialog):
    def __init__(self, task):
        super().__init__()
        self.setWindowTitle("Edit Task")
        layout = QVBoxLayout()

        # Task Input
        self.task_input = QLineEdit(task)
        layout.addWidget(self.task_input)

        # Ok & Cancel buttons
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def get_task(self):
        return self.task_input.text()

# This class represents the main window which holds all the tasks
class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Properties
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 400)

        # Layout
        self.layout = QVBoxLayout()

        # Task Input
        self.task_input = QLineEdit()
        self.layout.addWidget(self.task_input)

        # Add Task Button
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        # Display of Tasks
        self.tasks = []
        self.task_widgets = []

        # Set the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

    # Adds a task
    def add_task(self):
        task = self.task_input.text()

        if task:
            self.tasks.append(task)

            # Display the new list of tasks
            self.display_tasks()

    # Edits a task
    def edit_task(self,i):
        dialog = EditTaskDialog(self.tasks[i])
        task = dialog.get_task()

        if dialog.exec_():
            self.tasks[i] = task
            self.display_tasks()

    # Deletes a task
    def delete_task(self,i):
        del self.tasks[i]
        self.display_tasks()

    # Displays the tasks
    def display_tasks(self):

        # Clear old widgets
        for widget in self.task_widgets:
            self.layout.removeWidget(widget)
            widget.setParent(None)

        self.task_widgets = []

        for i, task in enumerate(self.tasks):
            label = QLabel(task)

            # Edit Button
            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda checked, i=i: self.edit_task(i))

            # Delete Button
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda checked, i=i: self.delete_task(i))

            # Layout for this task's info
            task_layout = QHBoxLayout()
            task_layout.addWidget(label)
            task_layout.addWidget(edit_button)
            task_layout.addWidget(delete_button)

            # Add to the main layout and widget list
            self.layout.addLayout(task_layout)
            self.task_widgets.extend([label, edit_button, delete_button])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Create an instance of the ToDoApp class
    todo_app = ToDoApp()
    todo_app.show()  # Display the main window

    # Start the application event loop
    sys.exit(app.exec_())
