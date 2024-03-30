from tkinter import *

class Calculator:
    def __init__(self):
        self.GUI = Tk()
        self.expression = ""
        self.operation = StringVar()

        self.GUI.configure(background="white")
        self.GUI.title("Calculator")
        self.GUI.geometry("375x375")

        self.create_widgets()

    def create_widgets(self):
        self.expression_field = Entry(self.GUI, textvariable=self.operation, font=('Colibry', 15),
                                      borderwidth=3, justify='right')
        self.expression_field.grid(row=0, column=0, columnspan=4, pady=5, ipadx=50, ipady=10)

        buttons_data = [
            ('7', '#ff0000'), ('8', '#ff7f00'), ('9', '#ffff00'), ('/', 'sky blue'),
            ('4', '#7fff00'), ('5', '#00ff00'), ('6', '#00ff7f'), ('*', 'sky blue'),
            ('1', '#00ffff'), ('2', '#007fff'), ('3', '#0000ff'), ('-', 'sky blue'),
            ('C', 'sky blue'), ('0', '#7f00ff'), ('=', 'sky blue'), ('+', 'sky blue')
        ]

        row_num = 1
        col_num = 0
        for (text, bg_color) in buttons_data:
            button = Button(self.GUI, text=text, fg='white', bg=bg_color, font=('Colibry', 15),
                            height=2, width=7, borderwidth=0, relief="groove")
            button.grid(row=row_num, column=col_num, pady=5, padx=5)

            if text == 'C':
                button.config(command=self.clear)
            elif text == '=':
                button.config(command=self.calculate)
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

    def run_calculator(self):
        self.GUI.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_calculator()