"""Welcome to Reflex!."""

from Climb_GUI import styles

# Import all the pages.
from Climb_GUI.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
# app.compile()
