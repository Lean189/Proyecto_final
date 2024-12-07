from django import template
from colorsys import rgb_to_hsv, hsv_to_rgb

register = template.Library()

@register.filter
def darken(value, factor=0.1):
    """Oscurece un color en formato hexadecimal."""
    if value.startswith("#"):
        value = value[1:]

    # Convertir el valor hex a RGB
    r = int(value[0:2], 16)
    g = int(value[2:4], 16)
    b = int(value[4:6], 16)

    # Convertir RGB a HSV para modificar el brillo
    r, g, b = rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    v = max(r, g, b)
    v = max(v - factor, 0.0)  # Oscurecer el brillo
    r, g, b = hsv_to_rgb(r, g, v)

    # Convertir RGB de vuelta a hexadecimal
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"
