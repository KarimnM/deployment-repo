import colorsys
import random


def hsv_to_rgb(hue_deg: float, saturation: float, brightness: float):
    if saturation > 1 or saturation < 0:
        raise ValueError("Saturation must be in range [0, 1], not '" + str(saturation) + "'")

    if brightness > 1 or brightness < 0:
        raise ValueError("Brightness must be in range [0, 1], not '" + str(brightness) + "'")

    r, g, b = colorsys.hsv_to_rgb(hue_deg / 360, saturation, brightness)
    return round(255 * r), round(255 * g), round(255 * b)


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def hsv_to_hex(hue_deg: float, saturation: float, brightness: float):
    return rgb_to_hex(hsv_to_rgb(hue_deg, saturation, brightness))


def generate_color_palette(num_colors, seed, saturation, brightness, hue_spread_deg=180):
    rand_gen = random.Random(seed)
    hues = []
    starting_hue = rand_gen.random() * 360
    hues += [starting_hue]
    if num_colors > 1:
        hue_increment = hue_spread_deg / (num_colors - 1)
        for i in range(1, num_colors):
            hue = starting_hue + hue_increment * i
            hue %= 360
            hues += [hue]

    rand_gen.shuffle(hues)
    hex_colors = [hsv_to_hex(hue, saturation, brightness) for hue in hues]
    return hex_colors


def test_color_palette_generator():
    random_seed = random.random()
    print(f"{random_seed=}")
    hex_colors = generate_color_palette(5, random_seed, 0.5, 0.8)
    print(hex_colors)
    print()
    for hex_color in hex_colors:
        print(f'\x1b[48;2;{int(hex_color[1:3], 16)};{int(hex_color[3:5], 16)};{int(hex_color[5:], 16)}m            '
              f'                    \033[0m')


if __name__ == '__main__':
    # run this in an rgb-enabled terminal to test the color palette generator
    test_color_palette_generator()
