import cv2

image = cv2.imread("output.png", cv2.IMREAD_COLOR)
width, height, _ = image.shape
middle_row = 200
barcode_string = ""
current_bar_width = 0
my_dict = {}
alphabets = [chr(ord('a') + i) for i in range(26)]
for i, char in enumerate(alphabets):
    barcode_width = i + 2
    my_dict[barcode_width] = char
for x in range(width):
    pixel = image[middle_row, x]
    if all(pixel == [0, 0, 0]): # Check if the pixel color is black (0, 0, 0).
        current_bar_width += 1
    else:
        if current_bar_width > 0:
            if current_bar_width == 1:
                barcode_string += ' '
            else:
                if current_bar_width in my_dict:
                    barcode_string += my_dict[current_bar_width]
            current_bar_width = 0
print("Reconstructed Barcode String:", barcode_string)