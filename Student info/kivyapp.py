import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):

    def __init__(self,**kwargs):
        super(MyGrid,self).__init__()
        self.cols = 2
        self.add_widget(Label(text='student name: '))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        self.add_widget(Label(text='student marks: '))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)
        self.add_widget(Label(text='student gender: '))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = "click me")
        self.press.bind(on_press = self.click_me )
        self.add_widget(self.press)


    def click_me(self,instance):
        print("name of student is " + self.s_name.text)
        print("marks of student is "+self.s_marks.text)
        print("gender of student is "+self.s_gender.text)


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()




