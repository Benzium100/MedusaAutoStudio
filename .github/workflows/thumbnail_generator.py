from PIL import Image, ImageDraw, ImageFont
import os

def main():
    img = Image.open("scene_1.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 10), "Medusa: Daily Epic", fill="white", font=font)
    img.save("thumbnail.png")
    print("Thumbnail generated!")

if __name__ == "__main__":
    main()
