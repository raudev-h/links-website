import reflex as rx
from web_project.styles.styles import *

def titles (text:str) -> rx.Component:
    return rx.heading(
        text,
        size="6",
        style=title_style,
    )