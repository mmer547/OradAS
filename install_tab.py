import flet as ft

class install_tab(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        container = ft.Container

        def open_repo(e):
            ft.page.launch_url('https://github.com/iqfareez/flet-hello')

        appbar = ft.AppBar(
            title=ft.Text(value="Flutter using Flet"),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            actions=[ft.IconButton(icon=ft.icons.CODE, on_click=open_repo)]
            )
        return appbar     

        # txt = ft.Text("テスト")             
        # return txt