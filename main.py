
import flet as ft
from git_control import GitControl 

def main(page: ft.Page):
    page.title = "Git Control"
    page.window_height = 500
    page.window_width = 1900
    page.add(
        ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.Container(
                        content=ft.Column([ 
                        GitControl("maincontroller"), 
                        GitControl("microcomputer")],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    )
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.SEARCH),
                    content=ft.Text("This is Tab 2"),
                ),            
            ]
        )
    )        

ft.app(target = main)

