"""Common templates used between pages in the app."""

from __future__ import annotations

from Climb_GUI import styles
from Climb_GUI.components.sidebar import sidebar
from typing import Callable

import reflex as rx

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


def menu_button() -> rx.Component:
    """The menu button on the top right of the page.

    Returns:
        The menu button component.
    """
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.menu(
            rx.menu_button(
                rx.icon(
                    tag="hamburger",
                    size="4em",
                    color=styles.text_color,
                ),
            ),
            rx.menu_list(
                *[
                    rx.menu_item(
                        rx.link(
                            page["title"],
                            href=page["route"],
                            width="100%",
                        )
                    )
                    for page in get_decorated_pages()
                ],
                # rx.menu_divider(),
                # rx.menu_item(
                #     rx.link("About", href="https://github.com/reflex-dev", width="100%")
                # ),
                # rx.menu_item(
                #     rx.link("Contact", href="mailto:founders@=reflex.dev", width="100%")
                # ),
            ),
        ),
        position="fixed",
        right="1.5em",
        top="1.5em",
        z_index="500",
    )

def top_bar():
    return rx.box(
        rx.hstack(
            rx.link(rx.image(src="/CLIMB_GUI_LOGO.png", height="4.0em"), href="/"),
            rx.box(
                rx.chakra.button_group( # was button group FIXME
                    # rx.link(rx.chakra.button("Profile", bg="black", color="white"), href="/Profile", button=True),
                    rx.link(rx.chakra.button("Start", bg="black", color="white"), href="/start", button=True),
                    # variant="outline",
                    is_attached=True,
                ),
                margin="10px"
            )
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        # Additional styling as needed
    )



def template(
    route: str | None = None,
    title: str | None = None,
    image: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template for each page of the app.

    Args:
        route: The route to reach the page.
        title: The title of the page.
        image: The favicon of the page.
        description: The description of the page.
        meta: Additionnal meta to add to the page.
        on_load: The event handler(s) called when the page load.
        script_tags: Scripts to attach to the page.

    Returns:
        The template with the page content.
    """

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.
        """
        # Get the meta tags for the page.
        all_meta = [*default_meta, *(meta or [])]
        
        @rx.page(
            route=route,
            title=title,
            image=image,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def templated_page():
            return rx.hstack(
                #sidebar(),
                top_bar(),
                rx.box(
                    rx.box(
                        page_content(),
                        **styles.template_content_style,
                    ),
                    **styles.template_page_style,
                ),
                rx.spacer(),
                #menu_button(),
                align_items="flex-start",
                transition="left 0.5s, width 0.5s",
                position="relative",
                background_color="black",
                #background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                background_image="linear-gradient(0deg,#1f1e1d,#000000)",
            )
        
            return templated_page

    return decorator
