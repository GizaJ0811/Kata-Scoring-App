from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
BoxLayout:
    size_hint: root.size
    MDRectangleFlatButton:
        text: "tell a secret"
        pos_hint: {"center_x": .5, "center_y": .5}
"""

class MyApp(MDApp):
    def build(self):
        self.title = "Scoring App"
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()