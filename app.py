import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class childApp(GridLayout):#here we are going to define the structure of the app
    def __init__(self,**kwargs):#// kwargs are use to perform multiple arguments
        super(childApp,self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Student name'))
        self.s_name = TextInput()#location where the student name is saved
        self.add_widget(self.s_name)

        self.add_widget(Label(text = 'Student marks'))
        self.s_marks = TextInput()#location where the student name is saved
        self.add_widget(self.s_marks)

        self.add_widget(Label(text = 'Student gender'))
        self.s_gender = TextInput()#location where the student name is saved
        self.add_widget(self.s_gender)

        self.press = Button(text ='click_me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        print(self.s_name.text)
        print(self.s_marks.text)
        print(self.s_gender.text)
        print('')

class parentApp(App):
    def build(self):#building of app started
        return childApp()
if __name__ == "__main__":
    parentApp().run()

