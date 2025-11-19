from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1280, 720), color=(30, 30, 30))
d = ImageDraw.Draw(img)
font = ImageFont.load_default()
d.text((50,300), "Medusa: Daily Adventure", fill=(255,0,0), font=font)
img.save("thumbnail.png")
