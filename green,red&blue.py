#https://flet.dev/docs/controls/slider/
#https://www.google.com/search?q=white+hexaminal+code&sca_esv=b7153bb7f0eb1afc&sxsrf=AHTn8zrsLF73vLvlzhuJH5nO6dNo0pwkBA%3A1744424460126&ei=DM75Z9S3B4aJwbkP7uTqyAE&ved=0ahUKEwjU7aHCt9GMAxWGRDABHW6yGhkQ4dUDCBA&uact=5&oq=white+hexaminal+code&gs_lp=Egxnd3Mtd2l6LXNlcnAiFHdoaXRlIGhleGFtaW5hbCBjb2RlMgQQIxgnMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESKMiUABYpx9wAHgBkAEAmAHjAaAB7hOqAQYwLjE0LjK4AQPIAQD4AQGYAgygAuUPwgIKECMYgAQYJxiKBcICBhAAGAcYHsICCxAAGIAEGJECGIoFwgIFEAAYgATCAgQQABgewgIHEAAYgAQYCsICCBAAGAcYCBgewgIHEAAYgAQYDcICBhAAGA0YHpgDAOIDBRIBMSBAkgcGMC4xMC4yoAfCXbIHBjAuMTAuMrgH5Q8&sclient=gws-wiz-serp
import flet as ft  

def main(page: ft.Page):
    page.title = "red, green and blue"
    page.horizontal_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "#FFFFFF"

    def update_color(e=None):
        red = int(red_slider.value)
        green = int(green_slider.value)
        blue = int(blue_slider.value)

        page.bgcolor = f"#{red:02x}{green:02x}{blue:02x}"
        page.update()

    red_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color, active_color="red")
    green_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color, active_color="green")
    blue_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color, active_color="blue")

    page.add(
        ft.Column([
            red_slider,
            green_slider,
            blue_slider,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=400
        )
    )

    update_color()

ft.app(target=main)
