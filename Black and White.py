from PIL import Image
input_image = input("Enter image path")
output_image = "1_bw.jpg"
try:
    img = Image.open(input_image)
    bw = img.convert("L")
    bw.save(output_image)
    print("Done! Saved as:", output_image)
except FileNotFoundError:
    print("Image not found")
