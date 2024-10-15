from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import UploadFileForm
import pandas as pd
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            try:
                # Read the uploaded file based on its format
                if file.name.endswith('.xlsx'):
                    df = pd.read_excel(file)
                elif file.name.endswith('.csv'):
                    df = pd.read_csv(file)
                else:
                    return HttpResponse("Unsupported file format")

                # Generate a dynamic summary
                summary = (
                    f"File Name: {file.name}\n"
                    f"Total Rows: {df.shape[0]}\n"
                    f"Total Columns: {df.shape[1]}\n\n"
                    "Columns Summary:\n"
                )

                # Loop through each column to provide individual column summaries
                for col in df.columns:
                    unique_values = df[col].nunique()
                    summary += f"Column '{col}': {unique_values} unique values\n"

                # Render the summary page first
                context = {'summary': summary, 'email_status': None}
                try:
                    # Attempt to send the summary via email
                    send_mail(
                        subject='File Summary Report',
                        message=summary,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=['recipient@example.com'],
                    )
                    context['email_status'] = "Email sent successfully!"
                except Exception as email_error:
                    # Capture email error and show it on the page
                    context['email_status'] = f"Failed to send email: {email_error}"

                # Render the success page with the summary and email status
                return render(request, 'fileupload/success.html', context)

            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
    else:
        form = UploadFileForm()

    return render(request, 'fileupload/upload.html', {'form': form})
