import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.text(
            "© 2025 Web Yeez Clouds. All rights reserved.",
            class_name="text-center text-sm text-gray-300",
        ),
        class_name="w-full p-4 botom-0 inset-x-0",
    )
