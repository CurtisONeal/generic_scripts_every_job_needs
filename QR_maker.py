import importlib.util
import subprocess
import sys

# Check for the existence of qrcode package and its dependency the Pillow package
qrcode_spec = importlib.util.find_spec('qrcode')
pil_spec = importlib.util.find_spec('Pillow')  # PIL is actually called Pillow on PyPi
if qrcode_spec is None or pil_spec is None:
    print("Package 'qrcode' and/or 'Pillow' is not installed. Trying to install... so this can work.")
    # Python modules aren't all installed, attempt to install them
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'qrcode[pil]'])
        print("Packages 'qrcode' and 'Pillow' installed successfully!")
    except subprocess.CalledProcessError:
        print(
            "Failed to install 'qrcode' and/or 'Pillow'. Please, install them manually using 'pip install qrcode[pil]' command.")

import qrcode
# qrcode[pil]
# from qrcode.image.pure import PyPNGImage

# Instructions
print(f"This file will take in a URL and a filename and generate a QR code in the same directory.")

# The URL to encode
url_data = input(f"Enter url just as it is in your browser to generate a QR code for: ")  # Replace with your desired URL

# Desired filename prefix
file_name = input(f"Enter the desired filename without the dot file extension. Example: my_qrcode. \n(Hit return for 'QR_CODE' as a default): ")
file_name = file_name if file_name else 'QR_CODE'
file_name += '.png'

# Generate the QR code
img = qrcode.make(url_data )

# Save the QR code as an image file (e.g., PNG)
img.save(file_name)

print(f"QR code generated successfully as {file_name}.png")
