import flet as ft

class pass_tab(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        tf = [
            ft.TextField(
            label="OpenRadiossのインストールパス", 
            value="C:\OpenRadioss_win64\OpenRadioss",
            ),
            ft.TextField(
            label="OpenRadiossのインストールパス", 
            value="C:\OpenRadioss_win64\OpenRadioss",
            )
        ]
        return tf