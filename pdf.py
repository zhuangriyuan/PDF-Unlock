import os
import fitz

def unlock_pdf(input_path, output_path, password):
    # Remove any double quotes in the input path
    input_path = input_path.replace('"', '')

    # Open the PDF file and load it into fitz
    pdf_file = fitz.open(input_path)

    # Check if the PDF is encrypted
    if pdf_file.is_encrypted:
        # Attempt to authenticate with the provided password
        if pdf_file.authenticate(password):
            # If the password is correct, decrypt the PDF and save it to the output path
            pdf_file.save(output_path)
            print(f"Successfully unlocked PDF: {input_path} -> {output_path}")
        else:
            print(f"Incorrect password for PDF: {input_path}")
    else:
        print(f"PDF is not encrypted: {input_path}")

# Prompt the user for the input path and password
input_path = input("Enter the path to the encrypted PDF file: ")
#password = input("Enter the password to unlock the PDF file: ")
password = input("Enter Password: ")

# Set the output path to 'C:\Users\ken\Desktop\input_file_name_unlocked.pdf'
output_directory = r'C:\Users\ken\Desktop'
input_file_name = os.path.splitext(os.path.basename(input_path))[0]
output_file_name = input_file_name + '_unlocked.pdf'
output_path = os.path.join(output_directory, output_file_name)

unlock_pdf(input_path, output_path, password)
