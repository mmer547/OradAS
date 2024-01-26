import flet as ft

from install_tab import install_tab
from pass_tab import pass_tab

def main(page: ft.Page):

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="インストール",
                content=install_tab()
            ),
            ft.Tab(
                text="ファイルパス",
                content=ft.Container(
                    content=pass_tab()
                ),
            ),
            ft.Tab(
                text="CAD",
                content=ft.Container(
                    content=ft.Text("作成中")
                ),
            ),
            ft.Tab(
                text="メッシュ作成",
                content=ft.Text("作成中"),
            ),
            ft.Tab(
                text="条件設定",
                content=ft.Text("作成中"),
            ),
            ft.Tab(
                text="計算実行",
                content=ft.Text("作成中"),
            ),
            ft.Tab(
                text="結果処理",
                content=ft.Text("作成中"),
            ),
        ],
        expand=1,
    )

    page.add(t)

ft.app(target=main)