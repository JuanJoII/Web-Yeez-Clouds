import reflex as rx
import asyncio
import random
from ..constants import INDEX_IMAGES_LIST


class ImageState(rx.State):
    src1: str = ""
    src2: str = ""
    fade: bool = False

    @rx.event(background=True)
    async def update_images(self):
        images = INDEX_IMAGES_LIST
        while True:
            async with self:
                self.fade = True
            await asyncio.sleep(0.5)

            new_src1, new_src2 = random.sample(images, 2)

            async with self:
                self.src1 = new_src1
                self.src2 = new_src2
                self.fade = False

            await asyncio.sleep(5)


def index_comp() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.image(
                    src=ImageState.src1,
                    class_name=rx.cond(
                        ImageState.fade,
                        "w-full h-full object-cover opacity-0 transition-opacity duration-500 ease-in-out",
                        "w-full h-full object-cover opacity-100 transition-opacity duration-500 ease-in-out",
                    ),
                ),
                class_name="w-full aspect-[9/14] h-screen",
            ),
            rx.box(
                rx.image(
                    src=ImageState.src2,
                    class_name=rx.cond(
                        ImageState.fade,
                        "w-full h-full object-cover opacity-0 transition-opacity duration-500 ease-in-out",
                        "w-full h-full object-cover opacity-100 transition-opacity duration-500 ease-in-out",
                    ),
                ),
                class_name="w-full aspect-[9/14] h-screen",
            ),
            spacing="0",
        ),
        class_name="w-full h-screen",
        on_mount=ImageState.update_images,
    )
