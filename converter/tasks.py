# converter/tasks.py
from celery import shared_task
from .models import Document
import fitz
from django.core.files.base import ContentFile
import os

# converter/tasks.py

@shared_task
def convert_document_task(document_id):
    """
    A Celery task to perform the PDF to SVG conversion asynchronously.
    """
    try:
        document = Document.objects.get(id=document_id)
        document.status = Document.Status.PROCESSING
        document.save(update_fields=['status'])

        source_path = document.source_pdf.path
        pdf_doc = fitz.open(source_path)

        page = pdf_doc[0]
        svg_content = page.get_svg_image(text_as_path=False)
        pdf_doc.close()

        svg_filename = os.path.splitext(document.get_source_filename())[0] + ".svg"
        content_file = ContentFile(svg_content.encode('utf-8'))

        # Save the file content to the result_svg field
        document.result_svg.save(svg_filename, content_file, save=False)

        # Set the final status to COMPLETED
        document.status = Document.Status.COMPLETED

        # --- FIX: Save all changes to the database ---
        document.save()
        # ----------------------------------------------

    except Document.DoesNotExist:
        print(f"Document with ID {document_id} not found.")
        return
    except Exception as e:
        print(f"Error converting document ID {document_id}: {e}")
        try:
            document = Document.objects.get(id=document_id)
            document.status = Document.Status.FAILED
            document.save(update_fields=['status'])
        except Document.DoesNotExist:
            pass