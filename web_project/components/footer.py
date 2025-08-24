import reflex as rx
import datetime
from web_project.styles.colors import TextColor 
from web_project.styles.styles import Spacer


def footer()->rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            alt="Logotipo de raudev-h. Una \"erre\" y una \"hache\" dentro de un hexágono con el símbolo de python"),
        rx.link(
            f"2024-{datetime.date.today().year} próximamente nombre de empresa",
            size="2",
            color= TextColor.FOOTER.value
            ),
            rx.text("BUILDING SOFTWARE WITH ♥ FROM HAVANA TO THE WORLD"),
            align="center",
            padding_bottom= "2.2em",
            padding_x=Spacer.BIG.value,
            font_size="0.9em",
            spacing="0",
            color= TextColor.FOOTER.value
    )