from PIL import Image

def convert_rgba_to_rgb(image_path, save_path):
    
    png = Image.open(image_path)
    png.load()

    background = Image.new("RGB", png.size, (255, 255, 255))
    background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

    background.save(save_path)