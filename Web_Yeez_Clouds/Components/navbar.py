import reflex as rx


def navbar_links(text: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(text, class_name="text-2xl font-semibold"),
        href=href,
        class_name="text-decoration-none text-white hover:text-blue-500 transition-colors duration-300",
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.spacer(),
                rx.hstack(
                    navbar_links("Home", "/"),
                    rx.spacer(),
                    navbar_links("About", "/about"),
                    spacing="9",
                    align_items="center",
                    justify="center",
                ),
                rx.spacer(),
                rx.link(
                    rx.image(
                        src="/yz_logo.png",
                        class_name="w-32 h-auto object-contain",
                    ),
                    href="/",
                ),
                rx.spacer(),
                rx.hstack(
                    navbar_links("Store", "/store"),
                    navbar_links("Contact", "/contact"),
                    spacing="9",
                    align_items="center",
                    justify="center",
                ),
                rx.spacer(),
                justify="between",
                align_items="center",
                class_name="bg-transparent backdrop-blur-lg px-1 py-2 fixed top-0 left-0 right-0 z-50 rounded-b-lg",
            )
        )
    )
