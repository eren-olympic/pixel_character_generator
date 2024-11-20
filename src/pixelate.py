from PIL import Image

def pixelate(image: Image.Image, pixel_size: int) -> Image.Image:
    """Convert image to pixel art style"""
    small = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.Resampling.NEAREST
    )
    return small.resize(image.size, Image.Resampling.NEAREST)