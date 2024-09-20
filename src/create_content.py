import os
import pdfplumber
from typing import List, Optional


def extract_text_from_pdf(pdf_path: str) -> List[Optional[str]]:
    with pdfplumber.open(pdf_path) as pdf:
        return [page.extract_text() for page in pdf.pages]


def save_page_text(text: str, page_number: int, output_dir: str, pdf_name: str) -> None:
    output_path = os.path.join(output_dir, pdf_name, f"pg{page_number}.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Página {page_number} salva em {output_path}")


def process_pdf(pdf_path: str, output_dir: str) -> None:
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pages_text = extract_text_from_pdf(pdf_path)

    for page_number, text in enumerate(pages_text, start=1):
        if text:
            save_page_text(text, page_number, output_dir, pdf_name)
        else:
            print(f"Página {page_number} não contém texto ou está vazia.")


if __name__ == "__main__":
    process_pdf(
        pdf_path=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "files",
            "source",
            "data_driven__metric_design.pdf",
        ),
        output_dir=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "files",
            "generative",
            "data_driven__metric_design",
        ),
    )
