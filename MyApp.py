from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

KV = """
<ScoreInput@MDTextField>
    mode: "fill"
    icon_right: 'scoreboard'
    size_hint_x: .6
    pos_hint: {'center_x': .5}

<Main>
    Screen:
        MDCard:
            size_hint: .7, 0.7
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            orientation: 'vertical'
            MDLabel:
                text: "Score"
                halign: 'center'
                font_size: 25
                bold: True
                size_hint_y: None
                y: self.texture_size[1]
            MDBoxLayout:
                spacing: 10
                padding: 15
                orientation: 'vertical'
                size_hint: .9, .9
                pos_hint: {'center_x': 0.5,'center_y': 0.5}
                ScoreInput:
                    hint_text: 'Score'
                ScoreInput:
                    hint_text: 'Score2'
                MDFillRoundFlatButton: 
                    id: btn
                    pos_hint: {'center_x': .5,'center_y': .5}
                    text: "Submit"
                    color: 'blue'
        
"""
class Main(MDScreen):
    def __init__(self) -> None:
        super().__init__()
        
class MyApp(MDApp):
    def build(self):
        self.title = "Scoring App"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.theme_style = "Dark"
        return Main()
Builder.load_string(KV)
if __name__ == '__main__':
    MyApp().run()