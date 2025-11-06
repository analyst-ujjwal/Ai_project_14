from PIL import Image, ImageDraw, ImageFont

def add_caption_to_image(image_path: str, caption: str, output_path: str):
    """
    Adds text overlay to the generated meme image.
    """
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    font_size = int(img.width / 15)
    font = ImageFont.load_default()

    # Position caption at bottom
    text_w, text_h = draw.textsize(caption, font=font)
    position = ((img.width - text_w) / 2, img.height - text_h - 20)

    # Add black outline
    outline_range = 2
    for dx in range(-outline_range, outline_range + 1):
        for dy in range(-outline_range, outline_range + 1):
            draw.text((position[0] + dx, position[1] + dy), caption, font=font, fill="black")

    # Add white text
    draw.text(position, caption, fill="white", font=font)

    img.save(output_path)
    return output_path
