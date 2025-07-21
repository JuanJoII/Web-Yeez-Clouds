import reflex as rx

def navbar_links(text: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(text),
        href=href,
        class_name="text-decoration-none text-white hover:text-blue-500 transition-colors duration-300",
    )

def navbar() -> rx.Component:
    
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(src='/Logo_temp.png', width='50px', height='auto'),
                        href='/',
                    ),
                    rx.heading(
                        'Yeez Clouds',
                    ),
                    align_items='center',
                ),
                rx.spacer(),
                rx.hstack(
                    navbar_links('Home', '/'),
                    navbar_links('About', '/about'),
                    navbar_links('Contact', '/contact'),
                    navbar_links('Blog', '/blog'),
                    spacing = '5',
                    align_items = 'center',
                    justify='center',
                ),
                justify='between',
                align_items = 'center',
                class_name="bg-transparent backdrop-blur-sm p-4 shadow-md sticky top-0",
            )
        )
    )