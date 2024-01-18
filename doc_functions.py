import pdfrw
import os
import smtplib
import email_template
from email.message import EmailMessage
import mimetypes


# Takes in the template PDF and fills it out with a data dictionary
def fill_and_send_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0]['/Annots']

    for annotation in annotations:
        if annotation['/Subtype'] == '/Widget':
            if annotation['/T']:
                key = annotation['/T'][1:-1]  # Remove parentheses around the key
                if key in data_dict:
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )

    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


# Sends an email with a PDF attachment to the Law Firm
def send_email_with_pdf(recipient_email, recipient_name, timeslots, pdf_file_paths, sender_email, sender_password,
                        smtp_server, smtp_port, data_dict):
    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = "RightRoute: New Mandate Document Created"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    final_dict = {
        "name": data_dict["name"],
        "contact": data_dict["tNummer"] if data_dict["mail"] == "n.a." else data_dict["mail"],
        "case": data_dict["case_description"]
    }

    html_msg = email_template.mail_template_creation(recipient_name, "10.01.2024 9am-11am", "13.01.2024 4pm-5pm",
                                                     "empty",
                                                     final_dict["name"], final_dict["contact"], final_dict["case"])
    msg.add_alternative(html_msg, subtype='html')

    # Attach each PDF file from the list of file paths
    for pdf_file_path in pdf_file_paths:
        ctype, encoding = mimetypes.guess_type(pdf_file_path)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)

        # Extract the filename from the full path
        file_name = os.path.basename(pdf_file_path)

        with open(pdf_file_path, 'rb') as fp:
            msg.add_attachment(fp.read(), maintype=maintype, subtype=subtype, filename=file_name)

    # Send the email via SMTP
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)


