import reflex as rx
from web_project.components.link_button import link_button
from web_project.components.titles import titles 

def links()-> rx.Component:
    return rx.vstack(
        titles("Redes Sociales"),
        
        link_button("github","Github",
                    "Perfil y proyectos",
                "sky","https://github.com/raudev-h"),

        link_button("instagram", "Instagram", 
                    "Usuario de Instagram",
                "ruby","https://www.instagram.com/rau_05.h/"),
        
        
    )