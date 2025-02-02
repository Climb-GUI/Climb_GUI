from Climb_GUI.Climb_GUI import styles
from Climb_GUI import styles
from Climb_GUI.templates import template
from datetime import date

import reflex as rx

header = rx.heading(
    # "Welcome to Climb GUI!", 
    # "Gradient Text", 
    # color="white"
    "Welcome to Climb GUI",
    style={
        # "background_image": "linear-gradient(to right, #ffe259, #ffa751)",
        "background_image":"linear-gradient(144deg,#7F00FF,#E100FF)",
        "background_clip": "text",
        "color": "transparent",
        "webkit_background_clip": "text",
        "webkit_text_fill_color": "transparent",
        "moz_background_clip": "text",
        "moz_text_fill_color": "transparent",
    }
)

content = "With the help of computer-vision you can now scan any rock-climbing surface and receive a personalized path to get you to the top as efficiently as possible. Simply fill out your profile and then click START. Happy climbing!"
instructions_header = "Instructions:"
instructions_body1 = "1) Click on the PROFILE tab."
instructions_body2 = "2) Fill out your profile, including your name, a short biography, and your skill level. "
instructions_body3 = "3) Navigate to the START tab, and select a photo of the climbing wall from your computer (.png or .jpeg ONLY)."
instructions_body4 = "4) Once you upload a photo, type out the color of the holds on the specific route you want to climb (red, green, blue, orange, purple, yellow, or black)."
instructions_body5 = "5) Finally, click the upload button, and once the buffer finishes loading, reload the page."
instructions_body6 = "6) Now you can see the ideal path for you!"
instructions_body7 = "7) Repeat the process if you wish to select a different color or use a different image."
instructions_body8 = "8) Please only select one image at a time! You must repeat the process everytime you wish to map a route."

main = rx.text(content, style={"width": "100%"})
instruction_head = rx.text(instructions_header, style={"width": "100%"}, font_size="1.5em")
instructionsbody1 = rx.text(instructions_body1, style={"width": "100%"})
instructionsbody2 = rx.text(instructions_body2, style={"width": "100%"})
instructionsbody3 = rx.text(instructions_body3, style={"width": "100%"})
instructionsbody4 = rx.text(instructions_body4, style={"width": "100%"})
instructionsbody5 = rx.text(instructions_body5, style={"width": "100%"})
instructionsbody6 = rx.text(instructions_body6, style={"width": "100%"})
instructionsbody7 = rx.text(instructions_body7, style={"width": "100%"})
instructionsbody8 = rx.text(instructions_body8, style={"width": "100%"})

footer = rx.text(f"Copyright {date.today().year}")

# Combine the components into the main AppModule
main_comp = rx.vstack(
    header,
    main,
    rx.spacer(),
    instruction_head,
    instructionsbody1,
    instructionsbody2,
    instructionsbody3,
    instructionsbody4,
    instructionsbody5,
    instructionsbody6,
    instructionsbody7,
    instructionsbody8,
    *([rx.spacer()] * 8),
    footer,
)

@template(route="/", title="Home")
def index() -> rx.components:
    return main_comp
