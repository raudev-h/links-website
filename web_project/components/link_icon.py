import reflex as rx
from web_project.styles.styles import *

def link_icon(icon:str, url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            icon,
            width=Spacer.DEFAULT.value,
        ),
        href= url,
        is_external= True
    )