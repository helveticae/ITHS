# Simple rgb to hex converter

def rgb_to_hex(r: int, g:int ,b: int) -> str:
    """Converting three RGB values to their hex representation using :X while returning the hex value."""
    return ('{:X}{:X}{:X}').format(r, g, b)


if __name__ == "__main__":
    a = rgb_to_hex(13, 17, 23)
    print(a)