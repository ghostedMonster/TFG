import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)

from kivy.graphics.context_instructions import Color

class ScatterTextWidget(BoxLayout):

    text_color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)

    def change_label_color(self, *args):
        color = [random.random() for i in range(3)] + [1]
        self.text_color = color


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()
