import reflex as rx
from ..Components import navbar, footer


@rx.page("/about", title="Yeez Clouds | About Us")
def about_page() -> rx.Component:
    return rx.box(
        navbar.navbar(),
        rx.heading("About Us", class_name="text-4xl font-bold text-center my-8"),
        rx.text(
            "Welcome to the About Us page of Yeez Clouds. Here, you can learn more about our mission, vision, and the team behind the brand.",
            class_name="text-center text-lg my-4",
        ),
        rx.text(
            "Yeez Clouds is dedicated to bringing you the latest in fashion and style, with a focus on quality and innovation.",
            class_name="text-center text-lg my-4",
        ),
        footer.footer(),
        class_name="w-full h-screen flex flex-col items-center justify-center",
    )
