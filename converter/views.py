# converter/views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm
from .models import Document
from .tasks import convert_document_task

def document_upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            if not document.title:
                document.title = document.source_pdf.name
            document.save()

            convert_document_task.delay(document.id)
            return redirect('converter:document_upload')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    context = {
        'form': form,
        'documents': documents
    }
    return render(request, 'converter/document_upload.html', context)

def check_document_status_view(request, pk):
    """
    API endpoint for AJAX polling to get the real-time status of a document.
    Returns JSON data about the document's status and result URL.
    """
    # Use get_object_or_404 to gracefully handle cases where the document is not found.
    document = get_object_or_404(Document, pk=pk)

    data = {
        'status': document.get_status_display(),
        'status_code': document.status,
        'result_url': document.result_svg.url if document.result_svg else None,
    }
    return JsonResponse(data)