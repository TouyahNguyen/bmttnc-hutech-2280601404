import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    # Add a delimiter to indicate end of message
    binary_message += '1111111111111110'  # 16-bit delimiter

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(pixels[col, row])
            for channel in range(3):  # Iterate over R, G, B channels
                if data_index < len(binary_message):
                    # Replace LSB of pixel[channel] with bit from message
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            pixels[col, row] = tuple(pixel)
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = "encoded_image.png"
    img.save(encoded_image_path)
    print("Giấu tin thành công. File ảnh được lưu là:", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()
