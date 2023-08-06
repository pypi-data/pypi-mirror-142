import io
import pathlib
import time
from io import BytesIO
from typing import List

import click
import requests
from cairosvg import svg2png
from diskcache import FanoutCache
from PIL import Image, ImageDraw, ImageFont
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

cache = FanoutCache()


@cache.memoize()
def _get_scryfall(path: str):
    response = requests.get(f"https://api.scryfall.com/{path}")
    response.raise_for_status()

    time.sleep(0.1)
    return response


def get_set_image(set_three_letter_code: str):
    """
    Downloads the set svg from scryfall

    The scryfall api docs request that we don't make more than 10 requests per second.
    """
    set_info = _get_scryfall(f"sets/{set_three_letter_code}").json()

    icon_uri = set_info["icon_svg_uri"]

    icon_resp = requests.get(icon_uri)
    icon_resp.raise_for_status()

    return icon_resp.content


def get_set_name(set_three_letter_code: str):
    set_info = _get_scryfall(f"sets/{set_three_letter_code}").json()

    return set_info["name"]


def render_spine(set_three_letter_code: str, dpi: int = 600):
    """
    Renders the card spine as a pdf
    """
    print(f"Rendering {set_three_letter_code}")
    page_margin = 0.25
    width = int((11 - page_margin * 2) * dpi)

    height = 1 * dpi

    # Draw Set Icon
    set_icon_margin = int(0.1 * dpi)

    set_image = get_set_image(set_three_letter_code)

    svg_bytesio = io.BytesIO(set_image)

    raw_image = io.BytesIO()

    rlg = svg2rlg(svg_bytesio)

    svg2png(
        file_obj=svg_bytesio,
        write_to=raw_image,
        background_color="transparent",
        scale=(dpi - set_icon_margin * 2) / rlg.height,
    )

    pil_icon = Image.open(raw_image).convert("RGBA")

    # Create the spine image
    im = Image.new(size=(width, height), mode="RGBA")

    icon_area_width = int(dpi * 2.5)

    # Paste the set icon in on the left side
    im.alpha_composite(
        pil_icon, ((icon_area_width - pil_icon.width) // 2, set_icon_margin)
    )

    # Draw the set name
    draw = ImageDraw.Draw(im)

    font = ImageFont.truetype("fonts/Beleren2016-Bold.ttf", size=350)

    set_name = get_set_name(set_three_letter_code)

    text_size = draw.textsize(set_name, font)

    x_offset = icon_area_width

    draw.text(
        (x_offset + (width - x_offset - text_size[0]) / 2, (height - text_size[1]) / 2),
        set_name,
        fill=(0, 0, 0, 255),
        font=font,
    )

    return im


@click.command()
@click.argument("set_code", type=str, nargs=-1)
def render_spine_command(set_code: List[str]):
    dpi = 600

    ims = [render_spine(set_code, dpi=dpi) for set_code in set_code]

    # Stack images
    im = Image.new(size=(ims[0].width, 1 + (ims[0].height + 1) * len(ims)), mode="RGBA")
    for i, sub_im in enumerate(ims):
        im.paste(sub_im, (0, 1 + i * (ims[0].height + 1)))

    # Draw separating lines
    draw = ImageDraw.Draw(im)

    for i in range(0, len(ims) + 1):
        y = i * (ims[0].height + 1)
        # Draw the line
        line_greyness = 160
        draw.line(
            (0, y, ims[0].width, y),
            fill=(line_greyness, line_greyness, line_greyness, 255),
            width=3,
        )

    filename = "_".join(set_code) + ".png"

    pathlib.Path("renders/").mkdir(parents=True, exist_ok=True)

    im.save(f"renders/{filename}", dpi=(dpi, dpi))


if __name__ == "__main__":
    render_spine_command()
