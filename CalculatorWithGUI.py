from tkinter import *
from tkinter import scrolledtext
import datetime

class Calculator:
    def __init__(self):
        self.GUI = Tk()
        self.expression = ""
        self.operation = StringVar()
        self.log_file = "calculator_log.txt"

        self.GUI.configure(background="red")
        self.GUI.title("Calculator")
        self.GUI.geometry("375x410")

        self.create_widgets()

    def create_widgets(self):
        self.expression_field = Entry(
            self.GUI, 
            textvariable=self.operation, 
            font=('Colibry', 15), 
            borderwidth=3, 
            justify='right'
            )
        
        self.expression_field.grid(row=0, column=0, columnspan=4, pady=5, ipadx=50, ipady=10)

        buttons_data = [
            ('1', '#BB11FF'), ('2', '#BB11FF'), ('3', '#BB11FF'), ('+', '#4b9dff'),
            ('4', '#BB11FF'), ('5', '#BB11FF'), ('6', '#BB11FF'), ('-', '#60b2ff'),
            ('7', '#BB11FF'), ('8', '#BB11FF'), ('9', '#BB11FF'), ('*', '#76c8ff'),
            ('C', '#FF964F'), ('0', '#BB11FF'), ('=', '#08ff08'), ('/', '#8bddff'),
            ('M+', '#4b9dff'), ('MRC', '#60b2ff'), ('MC', '#76c8ff'), 
            ('View\nLOG', '#FFD700')
        ]

        row_Number = 1
        column_Number = 0

        for (text, bg_color) in buttons_data:
            button = Button(
                self.GUI, 
                text=text, 
                fg='white', 
                bg=bg_color, 
                font=('Colibry', 15), 
                height=2, 
                width=7, 
                borderwidth=0, 
                relief="groove"
                )
            button.grid(
                row=row_Number, 
                column=column_Number, 
                pady=5, 
                padx=5
                )

            if text == 'C':
                button.config(command=self.clear)
            elif text == '=':
                button.config(command=self.calculate)
            elif text == 'M+':
                button.config(command=self.save_to_memory)
            elif text == 'MRC':
                button.config(command=self.retrieve_from_memory)
            elif text == 'MC':
                button.config(command=self.clear_memory)
            elif text == 'View\nLOG':
                button.config(command=self.view_log)
            else:
                button.config(command=lambda t=text: self.press(t))

            column_Number += 1
            if column_Number > 3:
                column_Number = 0
                row_Number += 1

    def press(self, num):
        self.expression += str(num)
        self.operation.set(self.expression)

    def clear(self):
        self.expression = ""
        self.operation.set("")

    def calculate(self):
        try:
            result = eval(self.expression)
            self.operation.set(result)
            self.log_operation(self.expression + " = " + str(result))
        except Exception as e:
            self.operation.set("Error")
        finally:
            self.expression = ""
    
    def save_to_memory(self):
        value = self.operation.get()
        self.log_operation("M+ " + value)
        with open("memory.txt", "w") as file:
            file.write(value)

    def retrieve_from_memory(self):
        try:
            with open("memory.txt", "r") as file:
                value = file.read()
                self.expression += value
                self.operation.set(self.expression)
                self.log_operation("MRC " + value)
        except FileNotFoundError:
            self.operation.set("Nothing stored yet 🤓")

    def clear_memory(self):
        try:
            with open("memory.txt", "w") as file:
                file.write("")
                self.operation.set("Memory Cleared")
            self.log_operation("MC")
        except Exception:
            self.operation.set("Error clearing memory")

    def log_operation(self, operation):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"\n`{timestamp}`: {operation}"
        with open(self.log_file, "a") as file:
            file.write(log_entry + "\n")

    def view_log(self):
        log_window = Tk()
        log_window.title("Calculator Log")
        log_window.geometry("375x410")

        log_text = scrolledtext.ScrolledText(log_window, 
                                             wrap=WORD, 
                                             font=('Arial', 12, 'bold')
                                            )
        log_text.pack(expand=True, fill='both')

        with open(self.log_file, "r") as file:
            log_contents = file.read()
            log_text.insert(END, log_contents)
            log_text.config(state=DISABLED)

        log_window.mainloop()

    def run_calculator(self):
        self.GUI.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_calculator()