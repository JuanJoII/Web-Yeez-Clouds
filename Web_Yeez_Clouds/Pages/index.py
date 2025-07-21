import reflex as rx
from ..Components import navbar, index_images_comp, footer

@rx.page(route="/", title="Yeez Clouds | Index")
def pagina_principal() -> rx.Component:
    return rx.box(
        navbar.navbar(),
        rx.vstack(
            [
                index_images_comp.index_comp(),
                rx.text("Explore our collection of Yeez Clouds images.", class_name="text-center text-lg my-4"),
            ],
            class_name="w-full",
        ),
        footer.footer(),
        class_name="w-full",
    )