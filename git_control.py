import flet as ft
from command_control import CommandControl

class GitControl(ft.Row):
    """_summary_

    Args:
        ft (_type_): _description_
    """
    def __init__(self, target):
        super().__init__()

        self.cmd_ctl = CommandControl(target)

        # get git branch
        self.branch = self.cmd_ctl.get_branches()
        selected_branch = self.branch.copy()

        # get git commit hash
        self.commit_hash = self.cmd_ctl.get_commit_hash()
        selected_hash = self.commit_hash.copy()

        # set row data
        self.txt_main = ft.TextField(value=target,
                                     expand=1)
        
        self.search_text_for_branch = ft.TextField(label="search branch", 
                                                   on_change=self.on_chane_value_branch, 
                                                   hint_text="input search text",
                                                   filled=True,
                                                   prefix_icon=ft.icons.SEARCH,
                                                   expand=2)
        
        self.dropdown_branch = ft.Dropdown(options=self.select_key_options(selected_branch),
                                           label="select branch",
                                           expand=3)
        
        self.search_text_for_hash = ft.TextField(label="search hash", 
                                                 on_change=self.on_chane_value_hash, 
                                                 hint_text="input search text",
                                                 filled=True,
                                                 prefix_icon=ft.icons.SEARCH,
                                                expand=2)
        
        self.dropdown_hash = ft.Dropdown(options=self.select_key_options(selected_hash),
                                         label="select hash",
                                         expand=3)
        
        self.pull_btn = ft.ElevatedButton(text="Pull", 
                                          on_click=self.exec_pull)

        self.checkout_branch_btn = ft.ElevatedButton(text="Checkout branch", 
                                               on_click=self.exec_checkout_branch)

        self.checkout_hash_btn = ft.ElevatedButton(text="Checkout hash", 
                                               on_click=self.exec_checkout_hash)


        self.controls= [
            self.txt_main,
            self.search_text_for_branch,
            self.dropdown_branch,                    
            self.search_text_for_hash,
            self.dropdown_hash,
            self.pull_btn,
            self.checkout_branch_btn,
            self.checkout_hash_btn,
        ]
        self.width = 1600
        self.alignment=ft.MainAxisAlignment.CENTER,
        self.vertical_alignment=ft.CrossAxisAlignment.CENTER

    def on_chane_value_branch(self, e):
        """

        Args:
            e (_type_): _description_
        """
        selected_branch = [branch for branch in self.branch if self.search_text_for_branch.value in branch]
        self.dropdown_branch.options = self.select_key_options(selected_branch)
        self.update()       


    def on_chane_value_hash(self, e):
        """

        Args:
            e (_type_): _description_
        """
        selected_hash = [hash for hash in self.commit_hash if self.search_text_for_hash.value in hash]
        self.dropdown_hash.options = self.select_key_options(selected_hash)
        self.update()       


    def select_key_options(self, selected_text):
        """_summary_

        Returns:
            _type_: _description_
        """
        key_option = [ft.dropdown.Option(text=text) for text in selected_text]
        return key_option

    def exec_pull(self,e):
        self.cmd_ctl.exec_pull()

    def exec_checkout_branch(self,e):
        self.cmd_ctl.exec_checkout(self.dropdown_branch.value)

    def exec_checkout_hash(self,e):
        self.cmd_ctl.exec_checkout(self.dropdown_hash.value)