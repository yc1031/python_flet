
import flet as ft
from git_control import GitControl 

def main(page: ft.Page):
    page.title = "Git Control"
    page.verticle_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.add(
        ft.Tabs(
            selected_index=1,
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.Container(
                        content=ft.Column([ 
                        GitControl("maincontroller"), 
                        GitControl("microcomputer")])
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

