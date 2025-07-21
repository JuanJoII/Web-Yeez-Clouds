import reflex as rx

class LightGalleryComponent(rx.Component):
    library = '/public/lightgallery'
    tag = "LightGalleryComponent"
    is_default = False

    # define las props
    images: list[str]


def light_gallery(images: list[str]) -> rx.Component:
    return LightGalleryComponent(images=images)