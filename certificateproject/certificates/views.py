from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from django.core.mail import send_mail
from django.utils.html import strip_tags
from .forms import CertificateForm


def generate_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            student_email = form.cleaned_data['student_email']
            course_name = form.cleaned_data['course_name']
            completion_date = form.cleaned_data['completion_date']

            context = {
                'student_name': student_name,
                'course_name': course_name,
                'completion_date': completion_date
            }

            # Generate PDF
            template = get_template('certificate_pdf.html')
            html = template.render(context)
            buffer = BytesIO()
            pisa.CreatePDF(html, dest=buffer)

            # Send Email
            subject = "Course Completion Certificate"
            html_message = render_to_string('certificate_email.html', context)
            plain_message = strip_tags(html_message)

            send_mail(
                subject,
                plain_message,
                'admin@example.com',
                [student_email],
                html_message=html_message
            )

            # Download PDF
            response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{student_name}_certificate.pdf"'
            return response
    else:
        form = CertificateForm()

    return render(request, 'certificate_form.html', {'form': form})
