"""The settings page."""

from Climb_GUI.templates import template
from Climb_GUI.state import State
from typing import List

import reflex as rx

difficulties: List[str] = ["Beginner (vIntro-v1)", "Easy (v2-v4)", "Medium (v5-v7)", "Hard (v8-v10)", "Pro (v11-v12+)"]

class ProfileState(State):
    name: str = "Please enter your name."
    bio: str = "Please enter your bio."
    difficulty: str = "No selection yet."
   
    def set_difficulty(self, difficulty: str):
        self.difficulty = difficulty
    
    def handle_submit(self):
        
        print(self.name)
        print(self.bio)
        

@template(route="/Profile", title="Profile")
def profile() -> rx.Component:
    """The profile page.

    Returns:
        The UI for the profile page.
    """

    return rx.vstack(
        rx.heading("Name: " + ProfileState.name),
        rx.text("Bio: " + ProfileState.bio, font_size="1.5em", style={"text-wrap": "wrap"}),        
        rx.text("Experience: " + ProfileState.difficulty, font_size="1.5em"),
        rx.input(placeholder="What is your name?", on_blur=ProfileState.set_name),
        rx.input(placeholder="Enter a brief bio", on_blur=ProfileState.set_bio),
        rx.select(
            difficulties,
            placeholder="Select an example.",
            on_change=ProfileState.set_difficulty, # This triggers set_option method when an option is selected
            color_schemes="twitter",
        ),
    )


