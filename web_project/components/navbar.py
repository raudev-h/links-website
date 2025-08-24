import reflex as rx
from web_project.styles.styles import *
from web_project.styles.colors import Color 


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("rau", as_= "span", color= Color.PRIMARY.value, size="5",),
            rx.text("dev-h", as_= "span", color= Color.SECONDARY.value, size="5"),
            style=navbar_title_style,
        ),
        
        position="sticky",
        padding_x=Spacer.DEFAULT.value,
        padding_y=Spacer.SMALL.value,
        z_index="999",
        top="0",
        bg= Color.CONTENT.value
        
    )