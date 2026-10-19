import os
from PIL import Image, ImageDraw, ImageFont

def generate_icons():
    icons_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'icons')
    os.makedirs(icons_dir, exist_ok=True)

    sizes = [
        ('apple-touch-icon.png', 180),
        ('icon-192.png', 192),
        ('icon-512.png', 512)
    ]

    for filename, size in sizes:
        img = Image.new('RGBA', (size, size), (11, 15, 25, 255)) # Fintech dark #0B0F19
        draw = ImageDraw.Draw(img)

        # Draw rounded rectangle background with subtle gradient border
        margin = int(size * 0.04)
        corner_radius = int(size * 0.22) # iOS standard squircle feel
        
        # Outer glow border
        draw.rounded_rectangle(
            [margin, margin, size - margin, size - margin],
            radius=corner_radius,
            fill=(15, 23, 42, 255),
            outline=(20, 184, 166, 200),
            width=max(2, int(size * 0.015))
        )

        # Inner badge
        inner_m = int(size * 0.12)
        inner_r = int(size * 0.16)
        draw.rounded_rectangle(
            [inner_m, inner_m, size - inner_m, size - inner_m],
            radius=inner_r,
            fill=(13, 148, 136, 40), # Teal tint
            outline=(13, 148, 136, 120),
            width=max(1, int(size * 0.008))
        )

        # Draw stylized upward financial chart bars / shield layers
        center_x = size // 2
        center_y = int(size * 0.44)
        
        # 3 ascending bars
        bar_w = int(size * 0.09)
        spacing = int(size * 0.035)
        base_y = int(size * 0.60)
        
        # Bar 1 (Left - Cyan/Teal)
        h1 = int(size * 0.16)
        x1 = center_x - bar_w - spacing - (bar_w // 2)
        draw.rounded_rectangle(
            [x1, base_y - h1, x1 + bar_w, base_y],
            radius=int(bar_w * 0.3),
            fill=(20, 184, 166, 230)
        )

        # Bar 2 (Middle - Emerald)
        h2 = int(size * 0.26)
        x2 = center_x - (bar_w // 2)
        draw.rounded_rectangle(
            [x2, base_y - h2, x2 + bar_w, base_y],
            radius=int(bar_w * 0.3),
            fill=(16, 185, 129, 255)
        )

        # Bar 3 (Right - Amber Gold high peak)
        h3 = int(size * 0.36)
        x3 = center_x + (bar_w // 2) + spacing
        draw.rounded_rectangle(
            [x3, base_y - h3, x3 + bar_w, base_y],
            radius=int(bar_w * 0.3),
            fill=(245, 158, 11, 255)
        )

        # Draw trending arrow / diamond peak on Bar 3
        star_y = base_y - h3 - int(size * 0.035)
        star_r = int(size * 0.03)
        draw.ellipse(
            [x3 + (bar_w // 2) - star_r, star_y - star_r, x3 + (bar_w // 2) + star_r, star_y + star_r],
            fill=(251, 191, 36, 255)
        )

        # Draw typography: "SPL" and "1"
        try:
            # Try to load Windows system font Arial / Segoe UI
            font_size = int(size * 0.16)
            font = ImageFont.truetype("arialbd.ttf", font_size)
            sub_font = ImageFont.truetype("arialbd.ttf", int(size * 0.08))
        except Exception:
            font = ImageFont.load_default()
            sub_font = ImageFont.load_default()

        # Text: SPL
        text = "SPL 1"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        text_x = center_x - (text_w // 2)
        text_y = int(size * 0.68)

        # Text shadow
        draw.text((text_x + 1, text_y + 1), text, fill=(0, 0, 0, 200), font=font)
        # Main text (White)
        draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)

        # Subtext: DÜZEY
        sub_text = "DÜZEY 1"
        sub_bbox = draw.textbbox((0, 0), sub_text, font=sub_font)
        sub_w = sub_bbox[2] - sub_bbox[0]
        sub_x = center_x - (sub_w // 2)
        sub_y = text_y + text_h + int(size * 0.03)
        draw.text((sub_x, sub_y), sub_text, fill=(20, 184, 166, 240), font=sub_font)

        out_path = os.path.join(icons_dir, filename)
        img.save(out_path, 'PNG', optimize=True)
        print(f"Generated {out_path} ({size}x{size})")

if __name__ == '__main__':
    generate_icons()
