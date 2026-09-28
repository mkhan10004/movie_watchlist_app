from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

folder = Path('assets/images')
folder.mkdir(parents=True, exist_ok=True)

movies = [
    ('inception.png', 'Inception', (18, 33, 71)),
    ('matrix.png', 'The Matrix', (43, 65, 85)),
    ('interstellar.png', 'Interstellar', (59, 86, 64)),
    ('arrival.png', 'Arrival', (92, 56, 68)),
    ('dune.png', 'Dune', (62, 41, 78)),
]

for file_name, title, color in movies:
    img = Image.new('RGB', (640, 960), color)
    draw = ImageDraw.Draw(img)

    for i in range(6):
        x0 = 40 + i * 90
        y0 = 120 + i * 80
        x1 = 600 - i * 90
        y1 = 840 - i * 80
        if x1 <= x0:
            x1 = x0 + 60
        if y1 <= y0:
            y1 = y0 + 60
        draw.rectangle(
            (x0, y0, x1, y1),
            outline=(255, 255, 255, 120),
            width=3,
        )

    try:
        font = ImageFont.truetype('arial.ttf', 60)
    except Exception:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (640 - text_width) // 2
    y = 420 - (text_height // 2)
    draw.text((x, y), title, font=font, fill=(255, 255, 255))
    img.save(folder / file_name)
    print(f'created {file_name}')
