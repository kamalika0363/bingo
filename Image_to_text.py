import easyocr
import os

# Initialize EasyOCR reader
reader = easyocr.Reader(["en"])  # 'en' for English, you can specify other languages too

# Load image
image_path = "E:/Glitch catchers/bingo/test.jpeg"

# Perform OCR on the image
result = reader.readtext(image_path)

# Extract text from the OCR result
extracted_text = ""
for detection in result:
    text = detection[1]
    extracted_text += text + "\n"

# Print the extracted text
print(extracted_text)
