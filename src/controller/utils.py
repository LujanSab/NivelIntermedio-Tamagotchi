import pygame


def scale_img(image, scale: float):
    """
    La función `scale_img` toma una imagen y la escala según un factor específico utilizando el método
    `transform.scale` de Pygame.

    parametros:
    ----------
        - image: El parámetro `image` es la imagen que desea escalar. Normalmente es un objeto de superficie
        que representa una imagen en Pygame
        - scale: El parámetro `scale` en la función `scale_img` se utiliza para determinar el factor
        por el cual se debe escalar la imagen. De manera predeterminada, está configurado en `Styles.DOG_IMAGE`, lo que sugiere que
        la imagen se escalará según un valor de escala predefinido para una imagen de perro. Puede
    
    return:
    -------
        - devuelve una nueva imagen que se ha escalado según el factor de escala especificado.
    """
    width = int(image.get_width() * scale)
    height = int(image.get_height() * scale)

    new_image = pygame.transform.scale(image, size=(width*scale, height*scale))
    
    return new_image