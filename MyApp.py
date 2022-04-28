from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
import sqlite3 as sql3
from kivymd.uix.menu import MDDropdownMenu

#=======================================================================

connect_db = sql3.connect('local_db.db')
cursor = connect_db.cursor()
data = cursor.fetchall()

#Author: @GizaJ0811
#=======================================================================
KV = """
<ScoreInput@MDDropDownItem>
    size_hint_x: .6
    pos_hint: {'center_x': .5}
    #on_release: root.scoredropdown()

<Main>
    Screen:
        MDCard:
            size_hint: .7, 0.7
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            orientation: 'vertical'
            MDLabel:
                text: "Score"
                halign: 'center'
                pos_hint: {'top': 1}
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
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        orientation: 'horizontal'
                        ScoreInput:
                            id: scr
                            on_release: root.scoredropdown(self)
                            font_size: 16
                        MDIconButton:
                            icon: 'scoreboard'
                    MDBoxLayout:
                        orientation: 'horizontal'
                        ScoreInput:
                        MDIconButton:
                            icon: 'scoreboard'
                MDFillRoundFlatButton: 
                    id: btn
                    pos_hint: {'center_x': .5,'center_y': .5}
                    text: "Submit"
                    on_press: root.submit_btn()
        
"""
#=======================================================================
class Main(MDScreen):
    def scoredropdown(self, instance):
        self.score_menu_list = [{
            "viewclass": "OneLineListItem",
            "text": str(i),
            "on_release": lambda _=str(i): self.set_score(_)
        } for i in range(5,11)]
        self.menu = MDDropdownMenu(
            items=self.score_menu_list,
            width_mult = 4,
            caller=instance
        ).open()
    def submit_btn(self):
        """Button function"""
    def set_score(self,score):
        self.ids.scr.set_item
        print(self.ids.scr.current_item)
        
class MyApp(MDApp):
    def build(self):
        self.title = "Scoring App"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.theme_style = "Dark"
        return Main()
Builder.load_string(KV)
if __name__ == '__main__':
    MyApp().run()