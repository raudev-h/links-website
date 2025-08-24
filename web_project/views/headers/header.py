import reflex as rx
from web_project.styles.styles import *
from web_project.components.link_icon import link_icon
from web_project.components.info_text import info_text
from web_project.styles.colors import TextColor 

def  header()-> rx.Component:
    return rx.vstack(
        rx.hstack(
                rx.avatar(
                        src="python.png",
                        fallback="RH",
                        size="6",
                        radius="full",
                        style= avatar_style
                        ),
                rx.vstack(
                        rx.heading(
                                "Raúl Hechavarria",
                                size="6"
                                ),
                rx.text(
                        "@raudev-h",
                        color= TextColor.BODY.value
                        ),
                rx.hstack(
                        link_icon(
                                "twitter",
                                "https://x.com/Raulh_05"
                                ),
                        link_icon(
                                "message-circle",
                                "https://wa.link/dsszvu",
                                )
                        ),
                spacing="0",
                align="start"
                ),
                spacing="5"
        ),

        rx.flex(
                info_text("0", "años de experiencia"),
                rx.spacer(),
                info_text("Meta:", "Arquitecto de software"),
                rx.spacer(),
                info_text("Lenguajes", "Python, Java, C"),
                width="100%"
        ),
        
        rx.text(
                "Soy estudiante de Ingeniería Informática de la Cujae desde el curso 2024-2025. " \
                "Actualmente estoy en 2do año de la carrera y este es mi primer proyecto web",
                color= TextColor.BODY.value,
                size="2",
                ),
        spacing= "5",

)