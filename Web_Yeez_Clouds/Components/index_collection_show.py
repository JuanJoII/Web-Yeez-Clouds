import reflex as rx


def collection_show() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src="/index_img_3.jpg",
                class_name="w-1/2 aspect-[3/4] object-cover",
            ),
            rx.box(
                rx.vstack(
                    rx.center(
                        rx.heading(
                            "Yeez Clouds Colección #1",
                            class_name="text-4xl font-bold text-center my-8",
                        )
                    ),
                    rx.text(
                        "Descubre la colección de Yeez Clouds, una serie de imágenes que capturan la esencia de la moda y el estilo.",
                        class_name="text-center text-lg my-4",
                    ),
                ),
                class_name="item-center justify-center",
            ),
        )
    )
