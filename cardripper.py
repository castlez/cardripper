import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def main():
    print("Welcome, to card ripper!")

    test_path = os.path.join("C:\\", "Projects", "images", "multie.jpg")
    # test_path = os.path.join("C:\\Projects\\hello.png")

    parts = test_path.split('.')
    bw_image_path = str(parts[0]) + "bw" + '.' + str(parts[1])

    if not os.path.exists(test_path):
        raise IOError(f"File '{test_path}' not found!")
    else:
        print("Found the image file!")

    print("Parsing image data...")
    image = Image.open(test_path)
    image.convert("L")
    # image.show()
    card_text = pytesseract.image_to_string(image)

    print("Card text:\n" + card_text)


if __name__ == "__main__":
    main()
