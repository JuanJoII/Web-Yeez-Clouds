import reflex as rx
from ..Components import navbar, index_images_comp, index_collection_show, footer


@rx.page(route="/", title="Yeez Clouds | Index")
def pagina_principal() -> rx.Component:
    return rx.box(
        navbar.navbar(),
        rx.vstack(
            [
                index_images_comp.index_comp(),
                index_collection_show.collection_show(),
            ],
            class_name="w-full",
        ),
        footer.footer(),
        class_name="w-full",
    )
