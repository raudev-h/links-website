import reflex as rx
from web_project.styles.styles import *

def link_button(icon:str, title:str, body:str, color:str, url:str) -> rx.Component:
    return rx.link(
        rx.button( 
            rx.hstack(
                rx.icon(
                    icon, 
                    width="28px",
                ),
                
                rx.vstack(
                    rx.text(title, style=button_title_style),
                    rx.text(body, style=button_body_style),
                    padding_right=Spacer.SMALL.value,
                    spacing="0",
                    flex="1",
                    align="start",
                    alt=title
                ),
            align="center",
            width="100%",
            spacing="4"
            ),
        color_scheme=color,
        variant="soft",
        width="100%"
    ),
        href=url,
        is_external=True,
        width="100%"
)