from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.scatter import Scatter


class Hello(MDApp):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = MDLabel(
                text = 'Hello',
                font_size = 150
        )

        f.add_widget(s)
        s.add_widget(l)
        return f

Hello().run()
