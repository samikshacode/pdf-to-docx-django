# PDF to MS Word Converter using Python & Django

## Task Overview

The objective of this project is to create an MS Word document from scratch
by reading and analyzing a given PDF file and replicating its content and layout
using Python.

## Approach

1. The application accepts a PDF file as input through a Django-based interface.
2. The PDF is read and parsed using the `pdfplumber` library.
3. Content such as headings, paragraphs, line breaks, and alignment is extracted.
4. A new MS Word document is created from scratch using `python-docx`.
5. The document structure is recreated logically to match the original PDF layout.
6. The generated Word file is made available for download.

## Technologies Used

- Python 3.x
- Django Framework
- pdfplumber (PDF text extraction)
- python-docx (MS Word document creation)

## Key Features

- Upload PDF file
- Extract and analyze PDF structure
- Recreate document in MS Word format
- Preserve headings, spacing, alignment, and readability
- Download converted Word document

## Limitations

Exact pixel-perfect replication is limited due to the inherent structure of PDF files.
However, logical layout, readability, and document structure are accurately preserved,
which is the standard approach in backend document processing systems.

## Live URL

(To be updated after deployment)

## Repository

Source code is available in this repository.
