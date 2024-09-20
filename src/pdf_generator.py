import os
from fpdf import FPDF
import re

class PDFGenerator:
    def __init__(self, input_dir: str, output_pdf: str):
        self.input_dir = input_dir
        self.output_pdf = output_pdf
        self.pdf = FPDF(orientation='P', unit='mm', format='A4')
        self.pdf.set_auto_page_break(auto=True, margin=15)
        
        self.pdf.add_font('ArialUnicode', '', '/System/Library/Fonts/Supplemental/Arial Unicode.ttf', uni=True)

    def add_page_with_content(self, content: str):
        self.pdf.add_page()

        self.pdf.set_font('ArialUnicode', '', 12)

        self.pdf.multi_cell(0, 10, content)

    def generate_pdf(self):
        def extract_page_number(file_name):
            match = re.search(r'pg(\d+)\.txt', file_name)
            return int(match.group(1)) if match else float('inf')

        sorted_files = sorted(os.listdir(self.input_dir), key=extract_page_number)

        for file_name in sorted_files:
            file_path = os.path.join(self.input_dir, file_name)

            if file_name.endswith(".txt") and os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                print(f"Adicionando conteúdo do arquivo {file_name} ao PDF.")
                self.add_page_with_content(content)

        self.pdf.output(self.output_pdf)
        print(f"PDF gerado e salvo em {self.output_pdf}")

if __name__ == "__main__":
    input_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "generative",
        "data_driven__metric_design",
        "ptbr"
    )

    output_pdf = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "source",
        "data_driven__metric_design_translated.pdf"
    )

    pdf_generator = PDFGenerator(input_dir=input_dir, output_pdf=output_pdf)
    pdf_generator.generate_pdf()
