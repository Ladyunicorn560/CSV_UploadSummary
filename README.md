# CSV_UploadSummary

This Django project enables users to upload CSV or Excel files, view detailed summaries, and optionally send the summary via email.

## Features
- **Upload CSV/Excel files** and view summaries.
- **Email the summary** to a specified address (configuration required).

## Usage
Upload a CSV or Excel file.
View the summary of the uploaded file.
If configured, the summary will be emailed; status will be displayed on the page.

## Troubleshooting
Email Issues: Verify your email settings and account security settings.
File Upload Failures: Ensure the file format is valid.

## Configure Email Settings
In `settings.py`, set your email credentials:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_mail'
EMAIL_HOST_PASSWORD = 'your_pswrd'



