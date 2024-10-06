from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image from a file
image_path = r'D:/my files/NOVA/AI/Untitled.jpg'  # Make sure to prefix the path with 'r' for a raw string

# Open the image
image = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text: \n", text)
