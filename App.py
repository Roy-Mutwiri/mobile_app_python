from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class CalculatorLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4

        self.add_widget(Button(text='7'))
        self.add_widget(Button(text='8'))
        self.add_widget(Button(text='9'))
        self.add_widget(Button(text='+'))

        self.add_widget(Button(text='4'))
        self.add_widget(Button(text='5'))
        self.add_widget(Button(text='6'))
        self.add_widget(Button(text='-'))

        self.add_widget(Button(text='1'))
        self.add_widget(Button(text='2'))
        self.add_widget(Button(text='3'))
        self.add_widget(Button(text='*'))

        self.add_widget(Button(text='.'))
        self.add_widget(Button(text='0'))
        self.add_widget(Button(text='C'))
        self.add_widget(Button(text='/'))

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()
