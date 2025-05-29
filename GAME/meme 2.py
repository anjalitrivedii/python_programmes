from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, top_text, bottom_text, output_path='meme_output.jpg', font_path='arial.ttf',
                  font_size=40):
    # Open image
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return

    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()
        print("Custom font not found. Using default font.")

    # Helper to calculate text size using textbbox
    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Outline function
    def draw_text_with_outline(text, pos):
        x, y = pos
        outline_range = 2
        for dx in range(-outline_range, outline_range + 1):
            for dy in range(-outline_range, outline_range + 1):
                draw.text((x + dx, y + dy), text, font=font, fill='black')
        draw.text((x, y), text, font=font, fill='white')

    # Top text
    if top_text:
        top_text = top_text.upper()
        text_width, text_height = get_text_size(top_text, font)
        top_position = ((width - text_width) / 2, 10)
        draw_text_with_outline(top_text, top_position)

    # Bottom text
    if bottom_text:
        bottom_text = bottom_text.upper()
        text_width, text_height = get_text_size(bottom_text, font)
        bottom_position = ((width - text_width) / 2, height - text_height - 20)
        draw_text_with_outline(bottom_text, bottom_position)

    # Save output
    img.save(output_path)
    print(f"Meme saved to: {output_path}")


# Example usage
generate_meme(
    image_path = r"C:\Users\anjal\Downloads\146a2d50-0a25-4c1e-a766-5963697d9acb.jpeg",
    top_text = '100 errors',
    bottom_text = 'sir:',
    font_path = 'arial.ttf',
    font_size = 50
)
