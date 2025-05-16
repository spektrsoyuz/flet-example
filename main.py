import flet as ft
from flet.core.checkbox import Checkbox
from flet.core.column import Column
from flet.core.control_event import ControlEvent
from flet.core.elevated_button import ElevatedButton
from flet.core.row import Row
from flet.core.text import Text
from flet.core.textfield import TextField


def main(page: ft.Page) -> None:
    page.title = 'Flet Example'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    # Setup our fields
    text_username: TextField = TextField(label='Username:', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password:', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='I agree to ...', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        print('Username:', text_username.value)
        print('Password:', text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # Link the functions to the UI
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Render the sign-up page
    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                     text_password,
                     checkbox_signup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP)
