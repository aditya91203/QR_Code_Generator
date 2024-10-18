import qrcode
import matplotlib.pyplot as plt

# Function to generate and display a QR code
def generate_qr_code(data):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR Code using matplotlib
    plt.imshow(img, cmap='gray')
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

# Example usage
data_to_encode = "https://www.example.com"  # Replace with your data
generate_qr_code(data_to_encode)
