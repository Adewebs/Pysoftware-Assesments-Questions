from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .utils import extract_questions_from_pdf
from .models import Question
from django.conf import settings  # Import settings for MEDIA_ROOT
import os


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']

            # Ensure MEDIA_ROOT exists and save the file in MEDIA_ROOT
            file_path = os.path.join(settings.MEDIA_ROOT, pdf_file.name)
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)  # Ensure the directory exists

            with open(file_path, 'wb+') as destination:
                for chunk in pdf_file.chunks():
                    destination.write(chunk)

            # Check if file exists before trying to read it
            if os.path.exists(file_path):
                # Extract questions from the saved PDF file
                questions = extract_questions_from_pdf(file_path)

                # Save extracted questions to the database
                for q in questions:
                    Question.objects.create(
                        question_main=q['question_main'],
                        a=q['a'],
                        b=q['b'],
                        c=q['c'],
                        d=q['d'],
                        e=q.get('e', '')  # Option E is optional
                    )

                return redirect('question_list')  # Redirect to the question list page
            else:
                return render(request, 'questions/upload_pdf.html',
                              {'form': form, 'error': 'File was not saved properly.'})
    else:
        form = PDFUploadForm()

    return render(request, 'questions/upload_pdf.html', {'form': form})


def question_list(request):
    # Fetch all questions from the database
    questions = Question.objects.all()

    # Pass the questions to the template for rendering
    return render(request, 'questions/question_list.html', {'questions': questions})