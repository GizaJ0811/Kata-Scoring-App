from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
import sqlite3 as sql3
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
#=======================================================================

connect_db = sql3.connect('local_db.db')
cursor = connect_db.cursor()
data = cursor.fetchall()

#Author: @GizaJ0811
#=======================================================================
KV = """
<ScoreInput@MDDropDownItem>
    text: "5"
    size_hint_x: .6
    pos_hint: {'center_x': .5}

Screen:
    MDLabel:
        text: "Score"
        halign: 'center'
        pos_hint: {'top': 1}
        font_size: 25
        bold: True
        size_hint_y: None
        y: self.texture_size[1]
    MDCard:
        size_hint: .7, 0.7
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        orientation: 'vertical'
        MDBoxLayout:
            spacing: 10
            padding: 15
            orientation: 'vertical'
            size_hint: .9, .9
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            MDBoxLayout:
                orientation: 'vertical'
                MDGridLayout:
                    id: score
                    cols: 4
                    orientation: 'lr-tb'
                    ScoreInput:
                        on_release: app.scoredropdown(self)
                    Label:
                        text: ","
                        size_hint: None, None
                        size: self.texture_size[0],self.texture_size[1]
                    ScoreInput:
                        on_release: app.scoredropdown(self)
                    MDIconButton:
                        icon: 'scoreboard'
            MDFillRoundFlatButton: 
                id: btn
                pos_hint: {'center_x': .5,'center_y': .5}
                text: "Submit"
                on_press: app.submit_btn()
        
"""
#=======================================================================
class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kv = Builder.load_string(KV)

    def scoredropdown(self, instance):
        self.score_menu_list = [{
            "viewclass": "OneLineListItem",
            "text": str(i),
            "on_release": lambda _=str(i): self.set_score(instance,_)
        } for i in range(5,11)]
        self.menu = MDDropdownMenu(
            items=self.score_menu_list,
            width_mult = 1,
            caller=instance,
            position = 'bottom'
        )
        self.menu.open()

    def set_score(self,widget,score):
        widget.set_item(score)
        self.menu.dismiss()

    def submit_btn(self):
        """Button function"""
        for child_score_input in reversed(self.kv.ids.score.children):
            if isinstance(child_score_input, MDDropDownItem):
                print(child_score_input.current_item)
                
    def on_start(self):
        for child_score in reversed(self.kv.ids.score.children):
            if isinstance(child_score, MDDropDownItem):
                child_score.set_item("5")
        return
         
    def build(self):
        self.title = "Scoring App"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.theme_style = "Dark"
        return self.kv
if __name__ == '__main__':
    MyApp().run()