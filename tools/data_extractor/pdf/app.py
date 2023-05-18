import os
import sys
import PyPDF2


def extract_text_from_pdf(pdf_path, output_file):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    with open(output_file, 'w', encoding='utf-8') as result_file:
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            result_file.write(f"Page {page_num + 1}:\n{text}\n\n")

    pdf_file.close()
    print(
        f"Extraction terminée. Le texte a été sauvegardé dans {output_file}.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Veuillez spécifier le chemin vers le fichier PDF en argument.")
    else:
        pdf_path = sys.argv[1]
        output_file = f"{os.environ['PDF_EXTRACTOR_PATH']}/exchange/{os.path.basename(pdf_path).replace('pdf', 'txt')}"
        extract_text_from_pdf(pdf_path, output_file)
