import pdfplumber
import pandas as pd
import json

def extract_data_from_pdf(pdf_path, output_json_path, output_excel_path):
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            # Extract words from the page with their bounding boxes
            words = page.extract_words()
            for word in words:
                # Append each word with its coordinates to the data list
                data.append({
                    'word': word['text'],
                    'x0': word['x0'],  # left x-coordinate
                    'top': word['top'], # top y-coordinate
                    'x1': word['x1'],  # right x-coordinate
                    'bottom': word['bottom'], # bottom y-coordinate
                    'page': page_number + 1  # page number (1-indexed)
                })

    # Save data to JSON
    with open(output_json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    # Save data to Excel
    df = pd.DataFrame(data)
    df.to_excel(output_excel_path, index=False)

# User input for PDF filename
a = input("Enter PDF Name (Without .pdf): ")

# Usage example
pdf_path = a + '.pdf'  # Path to your PDF file
output_json_path = 'output.json'
output_excel_path = 'output.xlsx'

extract_data_from_pdf(pdf_path, output_json_path, output_excel_path)

print("Data extraction complete!")