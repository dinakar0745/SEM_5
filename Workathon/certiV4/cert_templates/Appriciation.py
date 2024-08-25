from PIL import Image, ImageDraw, ImageFont

# Load the template
template_path = 'test_cert/Appriciation.png'  # Path to the template image
output_path = 'test_cert/certificate.png'  # Output path for the generated certificate
qr_path = 'test_cert/image.png'  # Path to the image you want to attach

# Open the images
certificate = Image.open(template_path)
qr = Image.open(qr_path)

# Convert the qr to RGBA mode if it isn't already
if qr.mode != 'RGBA':
    qr = qr.convert('RGBA')

# Resize the qr to be larger
qr_size = (150, 150)  # Adjust size as needed
qr = qr.resize(qr_size, Image.Resampling.LANCZOS)

# Define the position where you want to paste the qr
qr_position = (certificate.width - qr_size[0] - 20, certificate.height - qr_size[1] - 60)  # Move qr 60 pixels up from the bottom

# Paste the qr onto the certificate with alpha channel as the mask
certificate.paste(qr, qr_position, qr)

# Load fonts (adjust the size and font style as needed)
name_font = ImageFont.truetype("fonts/AlexBrush.ttf", 60)  # Name font
other_font = ImageFont.truetype("arial.ttf", 40)  # Other text font
tag_font = ImageFont.truetype("arial.ttf", 30)  # Font for the certificate ID tag

# Define positions for the text (adjust these based on your template)
name_position = (certificate.width // 2, 720)  # Center horizontally
# cert_type_position = (certificate.width // 2, 350)  # Center horizontally
# date_position = (certificate.width // 2, 450)  # Center horizontally

def draw_centered_text(draw, text, position, font, fill):
    # Get bounding box of the text
    if hasattr(draw, 'textbbox'):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    else:
        # For older Pillow versions
        text_width, text_height = draw.textsize(text, font=font)
    
    x = position[0] - text_width / 2
    y = position[1] - text_height / 2
    draw.text((x, y), text, fill=fill, font=font)

# Insert test text into the certificate
draw = ImageDraw.Draw(certificate)
draw_centered_text(draw, "Dinakar Pathakota", name_position, name_font, "black")  # Name
# draw_centered_text(draw, "Certificate of Achievement", cert_type_position, other_font, "black")  # Certificate type
# draw_centered_text(draw, "Date: 2024-08-21", date_position, other_font, "black")  # Date

# Define the certificate ID and its position
cert_id = "b03f1422-3883-4804-b5cc-5c1065af239a"
tag_position = (certificate.width // 2, certificate.height - 70)  # Center horizontally, 50 pixels from the bottom

# Draw the certificate ID tag
draw_centered_text(draw, cert_id, tag_position, tag_font, "black")

# Save the resulting image to a file
certificate.save(output_path)

print(f"Test certificate saved as {output_path}")
