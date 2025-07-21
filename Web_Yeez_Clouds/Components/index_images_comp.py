import reflex as rx


def index_comp() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.image(
                    src="/index_img_1.jpg",
                    class_name="w-full h-full object-cover",
                ),
                class_name="w-full aspect-[9/14] h-screen",
            ),
            rx.box(
                rx.image(
                    src="/index_img_2.jpg",
                    class_name="w-full h-full object-cover",
                ),
                class_name="w-full aspect-[9/14] h-screen",
            ),
            spacing="0",
        ),
        class_name="w-full h-screen hola",
    )
