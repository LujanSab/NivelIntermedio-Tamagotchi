from src.config import Styles
import pygame


def scale_img(image, scale = 1.0):
    """
    The function `scale_img` takes an image and scales it by a specified factor using pygame's
    `transform.scale` method.
    
    :param image: The `image` parameter is the image that you want to scale. It is typically a surface
    object representing an image in Pygame
    :param scale: The `scale` parameter in the `scale_img` function is used to determine the factor by
    which the image should be scaled. By default, it is set to `Styles.DOG_IMAGE`, which suggests that
    the image will be scaled based on a predefined scale value for a dog image. You can
    :return: The function `scale_img` returns a new image that has been scaled based on the specified
    scale factor.
    """
    width = int(image.get_width() * scale)
    height = int(image.get_height() * scale)

    new_image = pygame.transform.scale(image, size=(width*scale, height*scale))
    
    return new_image