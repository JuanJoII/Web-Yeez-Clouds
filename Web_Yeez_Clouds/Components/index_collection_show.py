import reflex as rx


def collection_show() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src="/index_img_3.jpg",
                class_name="w-full aspect-[3/4] object-cover h-screen",
            ),
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Yeez Clouds Colección #1",
                        class_name="text-4xl font-bold text-center my-8",
                    ),
                    rx.text(
                        "Descubre la colección de Yeez Clouds, una serie de imágenes que capturan la esencia de la moda y el estilo.",
                        class_name="text-center text-lg my-4",
                    ),
                    rx.link(
                        rx.button(
                            "Ver Colección",
                            class_name="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition-colors duration-300",
                        ),
                        href="/store",
                    ),
                    spacing="4",
                    class_name="items-center justify-center h-full",
                ),
                class_name="h-screen w-full flex justify-center items-center",
            ),
        ),
        class_name="w-full",
    )
