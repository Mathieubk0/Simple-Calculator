from tkinter import *

class Calculator:
    def __init__(self):
        self.GUI = Tk()
        self.expression = ""
        self.operation = StringVar()

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
            ('M+', '#4b9dff'), ('MRC', '#60b2ff'), ('MC', '#76c8ff')
        ]

        row_num = 1
        col_num = 0
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
                row=row_num, 
                column=col_num, 
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
            else:
                button.config(command=lambda t=text: self.press(t))

            col_num += 1
            if col_num > 3:
                col_num = 0
                row_num += 1

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
        except Exception as e:
            self.operation.set("Error")
        finally:
            self.expression = ""
    
    def save_to_memory(self):
        value = self.operation.get()
        with open("memory.txt", "w") as file:
            file.write(value)

    def retrieve_from_memory(self):
        try:
            with open("memory.txt", "r") as file:
                value = file.read()
                self.expression += value
                self.operation.set(self.expression)
        except FileNotFoundError:
            self.operation.set("Nothing stored yet 🤓")

    def clear_memory(self):
        try:
            with open("memory.txt", "w") as file:
                file.write("")
                self.operation.set("Memory Cleared")
        except Exception:
            self.operation.set("Error clearing memory")

    def run_calculator(self):
        self.GUI.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_calculator()