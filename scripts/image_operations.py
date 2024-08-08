from PIL import Image

def create_splash_screen(background_path, icon_path, output_path):
    background = Image.open(background_path).convert("RGBA")
    icon = Image.open(icon_path).convert("RGBA")

    bg_width, bg_height = background.size
    icon_width, icon_height = icon.size

    position = (
        (bg_width - icon_width) // 2,
        (bg_height - icon_height) // 2
    )

    composite = Image.new("RGBA", background.size)
    composite.paste(background, (0, 0))
    composite.paste(icon, position, icon)
    final_image = Image.alpha_composite(background, composite)

    final_image.save(output_path)
    print("splash screen created successfully.")
