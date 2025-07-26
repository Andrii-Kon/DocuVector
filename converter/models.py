# converter/models.py

import os
from django.db import models

class Document(models.Model):
    """
    Represents a single document conversion job from PDF to SVG.
    This model tracks the source file, the resulting file, and the status
    of the conversion process.
    """

    # Defines standardized choices for the conversion status to ensure data integrity.
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROCESSING = 'PROCESSING', 'Processing'
        COMPLETED = 'COMPLETED', 'Completed'
        FAILED = 'FAILED', 'Failed'

    # A user-provided title for easy identification of the conversion job.
    title = models.CharField(
        max_length=255,
        verbose_name="Document Title",
        blank=True
    )

    # The original PDF file uploaded by the user.
    # The `upload_to` parameter specifies a subdirectory within MEDIA_ROOT.
    source_pdf = models.FileField(
        upload_to='uploads/pdfs/',
        verbose_name="Source PDF"
    )

    # The generated SVG file. It is allowed to be null as it's populated
    # after a successful conversion.
    result_svg = models.FileField(
        upload_to='uploads/svgs/',
        blank=True,
        null=True,
        verbose_name="Result SVG"
    )

    # The current status of the conversion, using the predefined choices.
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Status"
    )

    # Timestamps to track record creation and last modification.
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        # Default ordering for querysets, showing the newest documents first.
        ordering = ['-uploaded_at']

    def __str__(self):
        """
        Returns a human-readable string representation of the object,
        primarily used in the Django admin interface.
        """
        return self.title

    def get_source_filename(self):
        """
        A helper method to return only the filename of the source PDF,
        stripping the directory path.
        """
        return os.path.basename(self.source_pdf.name)