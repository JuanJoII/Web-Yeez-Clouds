"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .Pages import index


global_style = {
    "font_family": "Plus Jakarta Sans, sans-serif",  # Agrega una fuente de respaldo
}

app = rx.App(
    style=global_style,  # Aplica el estilo global
)

app.add_page(index.pagina_principal)
