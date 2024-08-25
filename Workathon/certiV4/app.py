import ftplib
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import pandas as pd
import os
from utils.certificate_factory import CertificateFactory
import uuid
import random
import smtplib
from dotenv import load_dotenv
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


# FTP Configuration
FTP_SERVER = os.getenv('FTP_SERVER')
FTP_USER = os.getenv('FTP_USER')
FTP_PASS = os.getenv('FTP_PASS')
FTP_UPLOAD_DIR = os.getenv('FTP_UPLOAD_DIR')

def upload_to_ftp(local_file_path, remote_file_name):
    try:
        ftp = ftplib.FTP(FTP_SERVER)
        ftp.login(user=FTP_USER, passwd=FTP_PASS)

        # Force Passive Mode
        ftp.set_pasv(True)

        with open(local_file_path, 'rb') as file:
            ftp.storbinary(f'STOR {os.path.join(FTP_UPLOAD_DIR, remote_file_name)}', file)

        ftp.quit()
        print("File uploaded successfully")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.form['email']

    # Generate a random 6-digit OTP
    otp = random.randint(100000, 999999)

    # Log the generated OTP for debugging purposes
    print(f"Generated OTP: {otp}")

    # Send the OTP using Gmail SMTP server
    try:
        msg = MIMEText(f"Your OTP is: {otp}")
        msg['Subject'] = 'Your OTP'
        msg['From'] = os.getenv('SMTP_USER')
        msg['To'] = email

        # Gmail SMTP server details
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = int(os.getenv('SMTP_PORT'))
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')  # Use App Password if 2-Step Verification is enabled

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, [email], msg.as_string())

        session['email'] = email
        session['otp'] = otp
        flash('An OTP has been sent to your email address. Please check your inbox.', 'success')
        return redirect(url_for('verify'))

    except Exception as e:
        print(f"Error: {str(e)}")  # Log the error for debugging
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('index'))

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        if 'otp' in session and int(entered_otp) == session['otp']:
            session['user'] = {'email': session['email']}
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
            return redirect(url_for('verify'))
    return render_template('verify.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('home.html', email=session['user']['email'])
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/create_certificate', methods=['GET', 'POST'])
def generate_certificate():
    if 'user' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            file_path = os.path.join('static/certificates/', file.filename)
            file.save(file_path)

            df = pd.read_csv(file_path)
            certificate_factory = CertificateFactory()
            generated_files = []
            for _, row in df.iterrows():
                name = row['Name']
                percentage = row['Percentage']
                email = row['Email']  # Assuming the third column is 'Email'
                cert_type = request.form['certificate_type']
                unique_code = str(uuid.uuid4())  # Generate a unique code
                date_of_issue = pd.to_datetime('today').strftime('%Y-%m-%d')  # Assuming the issue date is today
                certification_topic = cert_type  # Or however you determine the certification topic

                # Ensure the create_certificate method returns exactly two values
                cert_file, qr_file = certificate_factory.create_certificate(name, percentage, cert_type, unique_code)

                # Upload to FTP server
                upload_to_ftp(cert_file, unique_code + '.pdf')
                upload_to_ftp(qr_file, unique_code + '.png')

                # Save generated files information
                generated_files.append({
                    'Name': name,
                    'File': cert_file,
                    'QR': qr_file,
                    'UniqueCode': unique_code,
                    'CertURL': f"http://vedardhagudapati.ddns.net/workathon/{unique_code}.pdf",
                    'QRURL': f"http://vedardhagudapati.ddns.net/workathon/{unique_code}.png"
                })

                # Send email with attachment and updated content
                send_email_with_attachment(
                    to_email=email,
                    file_path=cert_file,
                    filename=unique_code + '.pdf',
                    full_name=name,
                    date_of_issue=date_of_issue,
                    certification_topic=certification_topic,
                    percentage=percentage
                )

            return render_template('view_certificate.html', certificates=generated_files, cert_type=request.form['certificate_type'])

    return render_template('create_certificate.html')



def send_email_with_attachment(to_email, file_path, filename, full_name, date_of_issue, certification_topic, percentage):
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['Subject'] = 'Your Certification'
        msg['From'] = os.getenv('SMTP_USER')
        msg['To'] = to_email

        # Email body with updated content
        email_body = f"""Dear {full_name},

Congratulations on completing your certification! We are pleased to attach your certificate, which officially recognizes your achievement.

Certificate Details:
- Issued Date: {date_of_issue}
- Certification Topic: {certification_topic}
- Achieved Percentage: {percentage}%

We commend you on your dedication and hard work. Your accomplishment is a testament to your skills and commitment in {certification_topic}.

Should you have any questions or need further assistance, please do not hesitate to contact us at [Institute's Contact Details].

Once again, congratulations, and we wish you continued success in your future endeavors!

Best regards,

[Your Institution]
[Contact Information]
[Institution's Website]
"""
        body = MIMEText(email_body, 'plain')
        msg.attach(body)

        # Attach the certificate file
        with open(file_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='pdf')
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(attachment)

        # Gmail SMTP server details
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = int(os.getenv('SMTP_PORT'))
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')  # Use App Password if 2-Step Verification is enabled

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, [to_email], msg.as_string())

        print(f"Email sent to {to_email} with attachment {filename}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


@app.route('/certificates/<filename>')
def download_file(filename):
    return send_from_directory('static/certificates', filename)

# @app.route('/verify/<unique_code>')
# def verify_certificate(unique_code):
#     file_path = os.path.join('static/certificates/', f"{unique_code}.pdf")
#     metadata_path = file_path.replace('.pdf', '.txt')

#     if os.path.exists(file_path) and os.path.exists(metadata_path):
#         with open(metadata_path, 'r') as metadata_file:
#             metadata = metadata_file.read()

#         return render_template('verify_certificate.html',
#                                cert_url=f"http://vedardhagudapati.ddns.net/workathon/{unique_code}.pdf",
#                                metadata=metadata)
#     return "Certificate not found", 404

# New route for verifying certificates
@app.route('/verify_certificate', methods=['GET'])
def verify_certificate():
    certificate_id = request.args.get('certificate_id')
    certificate_url = f"http://vedardhagudapati.ddns.net/workathon/{certificate_id}.pdf"
    
    # Check if the certificate exists (you might want to implement a proper check here)
    if certificate_exists(certificate_url):
        return render_template('verify_certificate.html', certificate_url=certificate_url)
    else:
        error = "Certificate not found"
        return render_template('verify_certificate.html', error=error)

def certificate_exists(url):
    # Implement a check to see if the certificate exists at the given URL
    import requests
    response = requests.head(url)
    return response.status_code == 200



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
