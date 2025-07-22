"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .Pages import index, about_page


global_style = {
    "font_family": "Plus Jakarta Sans"
}

app = rx.App(
    style=global_style,
)

app.add_page(index.pagina_principal)
app.add_page(about_page.about_page)
