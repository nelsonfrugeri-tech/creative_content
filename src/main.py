import os
from application.pdf_processor import PDFProcessor

def main():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, 'files', 'source', 'doc.pdf')
    output_dir = os.path.join(current_dir, 'files', 'generate')
    translate = True

    processor = PDFProcessor(
        pdf_path=pdf_path,
        output_dir=output_dir,
        translate=translate
    )

    processor.process()

if __name__ == "__main__":
    main()
