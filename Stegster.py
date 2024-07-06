import stepic
from PIL import Image
import docx
import PyPDF2

print("*---------------------------*")

choice = input("Choose operation (encrypt/decrypt): ")

if choice.lower() == "encrypt":
    data_type = input("Choose data type to hide (text/doc/pdf): ")

    if data_type.lower() == "text":
        text = input("Input Text: ")
        img_file = input("Photo: ")

        try:
            img = Image.open(img_file)
        except Exception as e:
            print(f"Error: {e}")
            exit()

        img_stegano = stepic.encode(img, text.encode())
        output_file = "Stegano.png"
        img_stegano.save(output_file)
        print(f"Image encoded successfully! Saved as {output_file}")

    elif data_type.lower() == "doc":
        doc_file = input("Doc File: ")
        img_file = input("Photo: ")

        try:
            doc = docx.Document(doc_file)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        except Exception as e:
            print(f"Error: {e}")
            exit()

        try:
            img = Image.open(img_file)
        except Exception as e:
            print(f"Error: {e}")
            exit()

        img_stegano = stepic.encode(img, text.encode())
        output_file = "Stegano.png"
        img_stegano.save(output_file)
        print(f"Image encrypt successfully! Saved as {output_file}")

    elif data_type.lower() == "pdf":
        pdf_file = input("PDF File: ")
        img_file = input("Photo: ")

        try:
            pdf = PyPDF2.PdfFileReader(pdf_file)
            text = ""
            for page_num in range(pdf.numPages):
                text += pdf.getPage(page_num).extractText()
        except Exception as e:
            print(f"Error: {e}")
            exit()

        try:
            img = Image.open(img_file)
        except Exception as e:
            print(f"Error: {e}")
            exit()

        img_stegano = stepic.encode(img, text.encode())
        output_file = "Stegano.png"
        img_stegano.save(output_file)
        print(f"Image encoded successfully! Saved as {output_file}")

    else:
        print("Unsupported data type. Please choose text, doc, or pdf.")

elif choice.lower() == "decrypt":
    img_file = input("Stegano Image: ")

    try:
        img_stegano = Image.open(img_file)
    except Exception as e:
        print(f"Error: {e}")
        exit()

    decoded_text = stepic.decode(img_stegano)
    output_file = "decrypt_Text.txt"

    with open(output_file, "w") as f:
        f.write(decoded_text)

    print(f"decrypt Text saved successfully! Saved as {output_file}")

else:
    print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")

print("*---------------------------*")
