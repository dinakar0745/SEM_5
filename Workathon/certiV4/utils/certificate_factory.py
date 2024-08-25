import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
from datetime import datetime


class CertificateFactory:
    def init(self):
        self.template_path = 'static/certificates/'

    def create_certificate(self, name, percentage, cert_type, unique_code):
        filename = f"{unique_code}.pdf"
        file_path = os.path.join(self.template_path, filename)
        qr_data = f"http://vedardhagudapati.ddns.net/workathon/{unique_code}.pdf"

        qr = qrcode.make(qr_data)
        qr_path = file_path.replace('.pdf', '.png')
        qr.save(qr_path)

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")

        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        c.drawString(100, height - 100, f"Certificate of {cert_type}")
        c.drawString(100, height - 150, f"This is to certify that {name}")
        c.drawString(100, height - 200, f"Has achieved {percentage}%")
        c.drawString(100, height - 250, f"Date: {current_date}")
        c.drawString(100, height - 300, f"Issued at: {current_datetime}")

        qr_width, qr_height = 1.5 * inch, 1.5 * inch
        c.drawImage(qr_path, width - qr_width - 100, 100, width=qr_width, height=qr_height)

        c.save()

        metadata = {
            'Name': name,
            'Percentage': percentage,
            'Certificate Type': cert_type,
            'Unique Code': unique_code,
            'Date': current_date,
            'Issued At': current_datetime
        }
        metadata_file_path = file_path.replace('.pdf', '.txt')
        with open(metadata_file_path, 'w') as metadata_file:
            for key, value in metadata.items():
                metadata_file.write(f"{key}: {value}\n")

        return file_path, qr_path