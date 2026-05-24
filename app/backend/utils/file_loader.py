import os

import PyPDF2

from app.backend.utils.config_loader import (
    load_config
)


config = load_config()

DATASET_PATH = config[
    "dataset_path"
]


def load_rulebooks():

    """
    Load all PDF rulebooks.
    """

    pdf_files = [

        file

        for file in os.listdir(
            DATASET_PATH
        )

        if file.endswith(".pdf")

    ]

    return pdf_files


def extract_pdf_text(file_path):

    """
    Extract text from PDF.
    """

    extracted_pages = []

    with open(

        file_path,

        "rb"

    ) as file:

        pdf_reader = PyPDF2.PdfReader(
            file
        )

        for page_number, page in enumerate(

            pdf_reader.pages

        ):

            text = page.extract_text()

            extracted_pages.append({

                "page_number":
                page_number + 1,

                "text":
                text

            })

    return extracted_pages