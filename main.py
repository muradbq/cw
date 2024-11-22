import sys
import flet as ft


def main(page: ft.Page):
    app_version = "v0.0.1"
    page.title = "Cable Wizard  |  " + app_version
    page.theme_mode = "dark"
    page.window.icon = "static/logo/logo.png"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = False

    def auth(e):
        if user_login.value == 'test' and user_password.value == 'test':
            btn_auth.text = "yes"
        else:
            btn_auth.text = "no"
        page.update()

    def validate(e):
        if all([user_login.value, user_password.value]):
            btn_auth.disabled = False
        else:
            btn_auth.disabled = True

        page.update()

    user_login = ft.TextField(label='Login', width=200,
                              on_change=validate, value="test", border_color="blue")
    user_password = ft.TextField(
        label='Password', width=200, on_change=validate, value="test", border_color="blue")
    btn_auth = ft.OutlinedButton(
        text="Go", width=200, on_click=auth, disabled=True)

    page.add(
        ft.Row(
            [
                ft.Column([
                    ft.Text('Login : test | Password : test'),
                    user_login,
                    user_password,
                    btn_auth
                ])

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.update()
    pass


if __name__ == "__main__":
    # ft.app(target=main)
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
