import flet as ft
import subprocess

class PullGui(ft.UserControl):
    def __init__(self, page: ft.page):
        super().__init__()
        self.page = page

    def build(self):
        self.page.title = "Git Control"
        self.page.verticle_alignment = ft.MainAxisAlignment.CENTER

        txt_main = ft.TextField("maincontroller")
        self.select_brach = [ft.Dropdown(on_click=self.on_click_key, options=self.select_key_options())]

        self.page.add(
            ft.Row(
                [
                    ft.
                ]
            )
        )

def main(page: ft.Page):
    page.add(PullGui(page))

ft.app(target = main)
