# Stegster
Stegster is a Python script designed for steganography by P3psee (Az Daniel), which involves hiding text, DOCX, or PDF data within an image file. The tool supports encoding (encrypting) and decoding (decrypting) operations.

Technologies Used:

- Python: The primary programming language for the script.
- Stepic Library: Used for encoding and decoding messages in images.
- PIL (Python Imaging Library): Specifically the Image module from PIL for image processing.
- docx Library: For handling DOCX files.
- PyPDF2 Library: For handling and extracting text from PDF files.

Supported File Types:

-Images: For hiding data and retrieving hidden data.
-Text Files: Simple text strings can be hidden.
-DOCX Files: Microsoft Word documents.
-PDF Files: Portable Document Format files.

How to Use the Tool Step-by-Step
1. Install the required libraries using pip: pip install stepic pillow python-docx PyPDF2
2. Run the script by executing:python Stegster.py

Example Usage

Encrypting a Text Message:
1. Run the script "python Stegster.py"
2. Choose the operation: (encrypt/decrypt): encrypt
3. Choose data type to hide (text/doc/pdf): text
4. Input Text: This is a secret message.
5. Provide the image file path: "Photo: path/to/image.png"
6. Output: "Image encoded successfully! Saved as Stegano.png"

Decrypting a Message:
1. Run the script: python Stegster.py
2. Choose operation (encrypt/decrypt): decrypt
3. Provide the stegano image file path: "Stegano Image: path/to/Stegano.png"
4. Output: decrypt Text saved successfully! Saved as decrypt_Text.txt
