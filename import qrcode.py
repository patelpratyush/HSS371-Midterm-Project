import qrcode

# URL to encode into QR code
website_url = "https://drive.google.com/file/d/1MI4RrxuGoTgIzaf1m5V1xxlUvk_OlINa/view?usp=sharing"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("website_qr_code.png")

print("QR Code generated successfully!")
