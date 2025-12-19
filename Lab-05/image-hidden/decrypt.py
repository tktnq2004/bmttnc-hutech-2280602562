import sys
from PIL import Image

def decode_image(encoded_image_pth):
    img = Image.open(encoded_image_pth)
    width,height = img.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):
                binary_message += format(pixel[n], '08b')[-1]
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':
            break
        message += char
    
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
    encoded_image_pth = sys.argv[1]
    hidden_message = decode_image(encoded_image_pth)
    print("Hidden message:", hidden_message)
    
if __name__ == "__main__":
    main()