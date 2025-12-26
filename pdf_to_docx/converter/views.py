from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import pdf_to_docx
import os

# Create your views here.
def upload_pdf(request):
    if request.method=="POST" and request.FILES.get("pdf"):
        pdf_file=request.FILES["pdf"]
        fs=FileSystemStorage()
        pdf_name=fs.save(pdf_file.name,pdf_file)
        pdf_path=fs.path(pdf_name)

        output_path=os.path.join("media","output.docx")
        pdf_to_docx(pdf_path,output_path)

        return render(request,"upload.html",{
            "download":True
        })

    return render(request,"upload.html")