from pathlib import Path
import fitz  # PyMuPDF


def main():
    pdf_path = Path('Gilivindu Web Content.pdf')
    out_path = Path('extracted_pdf.txt')

    doc = fitz.open(pdf_path)
    lines: list[str] = []
    lines.append(f'FILE: {pdf_path.name}')
    lines.append('')

    for i, page in enumerate(doc, start=1):
        text = page.get_text('text')
        text = '\n'.join([ln.rstrip() for ln in text.splitlines()])
        lines.append(f'=== PAGE {i} ===')
        lines.append(text.strip())
        lines.append('')

    out_path.write_text('\n'.join(lines).strip() + '\n', encoding='utf-8')
    print(f'Wrote {out_path.resolve()}')


if __name__ == '__main__':
    main()
