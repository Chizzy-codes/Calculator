import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.label import Label


class CalculatorFunctions(App):

    # give various functions to the accociated buttons when clicked

    def add(self, other):
        pass

    def subtract(self, other):
        pass

    def multiply(self, other):
        pass

    def divide(self, other):
        pass

    def delete(self):
        pass

    def equate(self, item1, func, item2):
        pass

    def clear(self):
        pass

    def display(self):
        pass


class Interface(GridLayout):
    def __init__(self, **var_args):
        super(Interface, self).__init__(**var_args)
        self.cols = 5
        #self.rows = 6
        self.padding = 20
        self.spacing = 20
        #self.row_force_default = True
        #self.row_default_height = 100
        #self.size_hint = (None, None)
        #self.bind(minimum_size = self.setter('size'))
        #self.bind(height=self.setter('top'))
        #self.col_force_default = True
        #self.col_default_width = 105



        self.add_widget(Label(text="", size_hint_x=None, width=0.25, size_hint_y=None, height=0.25))
        self.add_widget(Label(text="", size_hint_x=None, width=0.25, size_hint_y=None, height=0.25))
        self.add_widget(Label(text="", size_hint_x=None, width=0.25, size_hint_y=None, height=0.25))
        self.add_widget(Label(text="", size_hint_x=None, width=0.25, size_hint_y=None, height=0.25))
        self.add_widget(TextInput(text="0", multiline=False, width=400, size_hint_y=None, height=80))


        for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
            self.add_widget(Button(text=str(x), size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='DEL', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='=', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='+', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='-', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='*', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='/', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='CE', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='.', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='%', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))
        self.add_widget(Button(text='^', size_hint_x=None, width=80, size_hint_y=None, height=80, bold=True))


class CalculatorApp(App):
    def build(self):
        Config.set('graphics', 'width', '520')
        Config.set('graphics', 'height', '600')

        return Interface()


if __name__ == '__main__':
    CalculatorApp().run()
