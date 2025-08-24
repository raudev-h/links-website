import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FontWeight

# Constants
MAX_WIDTH = "500px"

# Sizes
class Spacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.7em"
    BIG = "2em"
    EXTRA_BIG = "2.8em"

# Styles
BASE_STYLE = {
    "font_family":Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,

    rx.heading:{
        # "size":"6",
        "color": TextColor.HEADER.value, 
        "font_family":Font.TITLE.value,
        "font_weight":FontWeight.MEDIUM.value
    },
    rx.button:{
        "width":"100%",
        "min_height":"4.4em",
        # "height":"4.2vw",
        "padding": Spacer.SMALL.value,
        "border_radius": Spacer.DEFAULT.value,
        "overflow": "hidden",
        "white_space": "normal", 
        "text_align": "start",
        "display": "block",
        # "color": TextColor.HEADER.value,
        # "background_color": Color.CONTENT.value
        # "_hover":{
            # "background_color": Color.SECONDARY.value
        # }
    }
}

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa:wght@500;700&display=swap"
    
]

avatar_style =  {
    "border": "3px solid " + Color.AVATAR.value
    }

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    weight=FontWeight.MEDIUM.value,  # Medium
    font_size=Spacer.LARGE.value
)

title_style = dict(
    # size="6",
    font_weight=FontWeight.MEDIUM.value,
    padding_top=Spacer.SMALL.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    weight=FontWeight.MEDIUM.value,
    font_size= Spacer.DEFAULT.value,
    color= TextColor.HEADER.value
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.LIGHT.value,
    font_size= Spacer.MEDIUM.value,
    color= TextColor.BODY.value
)