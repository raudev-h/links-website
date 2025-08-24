import reflex as rx
from web_project.components.navbar import navbar
from web_project.components.footer import footer
from web_project.views.headers.header import header
from web_project.views.links.links import links
from web_project.styles.styles import *
# Aquí se guardan todas las variables que cambian durante 
# La ejecución, se llaman state vars
# Si no queremos que algo cambie usamos texto fijo y no clases

class MyState(rx.State):
    pass


def index()-> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width= MAX_WIDTH,
            align="center",
            spacing="2", 
            margin_y= Spacer.DEFAULT.value,
            padding=Spacer.BIG.value
        ),
    ),    
        footer(),
)


app = rx.App(
    style= BASE_STYLE,
    stylesheets= STYLESHEETS
)
app.add_page(
    index,
    title= "raudev-h | Web de links",
    description= "Hola soy Raúl Hechavarria, estudiante de ingeniería informática",
    image= "/logo.png"
    )