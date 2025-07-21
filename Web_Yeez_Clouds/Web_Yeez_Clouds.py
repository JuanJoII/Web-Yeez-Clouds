"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .Components import navbar
from .Pages import index
from rxconfig import config


global_style = {
    "font_family": "Plus Jakarta Sans, sans-serif", # Agrega una fuente de respaldo
}

app = rx.App(
    style=global_style, # Aplica el estilo global
)

app.add_page(index.pagina_principal)
