# QR Code Generator 📱

This is a simple Python-based QR code generator using the `qrcode` and `matplotlib` libraries. The script allows you to generate a QR code from any text or URL and display it as an image.

## Features

- Generate a QR code from any data (URL, text, etc.)
- Customizable QR code parameters (size, error correction, box size, border)
- Displays the generated QR code using `matplotlib`
- Simple and easy to use

## Requirements

Before running the script, make sure you have the following dependencies installed:

- **Python 3.x**
- **qrcode** library
    ```bash
    pip install qrcode[pil]
    ```
- **matplotlib** library
    ```bash
    pip install matplotlib
    ```

## How to Use

1. Clone or download the project files.
2. Install the required dependencies using the commands mentioned above.
3. Modify the `data_to_encode` variable in the script to encode the data you want in the QR code (e.g., a URL or text).
4. Run the Python script to generate and display the QR code.

### Example

In the code, you can replace the URL `"https://drive.google.com/file/d/12CmzoMMmKLOpkpmermzsuqdhEussFdv-/view?usp=sharing"` with any text or URL you want to encode into a QR code.(Just for refernce I have attached the url of my resume in this code):

```python
data_to_encode = "https://drive.google.com/file/d/12CmzoMMmKLOpkpmermzsuqdhEussFdv-/view?usp=sharing"
generate_qr_code(data_to_encode)
