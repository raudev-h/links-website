import reflex as rx
from web_project.styles.colors import Color 
from web_project.styles.styles import *

def info_text(title:str, body:str):
    return rx.box(
        rx.text(
            title, weight="bold", color= Color.PRIMARY.value , as_="span"
        ),
        f" {body}",
        font_size=Spacer.MEDIUM.value,
        color= TextColor.BODY.value 
    )