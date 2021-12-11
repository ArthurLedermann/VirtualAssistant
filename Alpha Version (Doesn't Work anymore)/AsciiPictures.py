import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=900):
    width, height = image.size 
    ratio = height/width
    new_height = int(new_width * ratio)-400
    resized_image= image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image=image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels=image.getdata()
    charachters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return charachters

path=r"C:\Users\arthu\Desktop\Alice Project\ClubBall.jpg"

def AsciiClub(path, new_width=900):
    image=PIL.Image.open(path)
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count=len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)