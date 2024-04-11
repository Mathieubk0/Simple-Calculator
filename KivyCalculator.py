from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(App):
    def build(self):
        self.expression = ""
        self.operation = TextInput(font_size=30, multiline=False, halign='right', readonly=True)

        layout = GridLayout(cols=4)
        layout.add_widget(self.operation)

        buttons_data = [
            ('1', '#BB11FF'), ('2', '#BB11FF'), ('3', '#BB11FF'), ('+', '#4b9dff'),
            ('4', '#BB11FF'), ('5', '#BB11FF'), ('6', '#BB11FF'), ('-', '#4b9dff'),
            ('7', '#BB11FF'), ('8', '#BB11FF'), ('9', '#BB11FF'), ('*', '#4b9dff'),
            ('C', 'sky blue'), ('0', '#FF964F'), ('=', '#08ff08'), ('/', '#4b9dff')
        ]

        for (text, bg_color) in buttons_data:
            button = Button(
                text=text,
                background_color=[0, 0, 0, 1] if text == '=' else [1, 1, 1, 1],
                color=[1, 1, 1, 1],
                font_size=30
            )
            button.bind(on_press=self.button_press)
            layout.add_widget(button)

        return layout

    def button_press(self, instance):
        button_text = instance.text

        if button_text == 'C':
            self.clear()
        elif button_text == '=':
            self.calculate()
        else:
            self.expression += button_text
            self.operation.text = self.expression

    def clear(self):
        self.expression = ""
        self.operation.text = ""

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.operation.text = result
        except Exception as e:
            self.operation.text = "Error"
        finally:
            self.expression = ""


if __name__ == "__main__":
    Calculator().run()