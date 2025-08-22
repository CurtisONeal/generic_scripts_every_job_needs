qr_code_readme.md

# QR Code - Make QR Codes for Free with Python

This is a standalone python script that creates a qrocode image from the commandline after aswering some questions.

It assumes that you can run python from the command line.

If you currently cannot, here is a tutorial:
https://realpython.com/run-python-scripts/

## Pre-requirements

This script uses the following python libraries. It is recommended you pip/pip3 install them first. If this is also new to you, please see: https://realpython.com/what-is-pip/

Packages:

importlib.util
subprocess
sys
qrcode
pil_spec (this should come in as a dependency of qrcode)

# Usage:

## Prompts

$ ./QR_maker.py
$ This file will take in a URL and a filename and generate a QR code in the same directory.
$ Enter url just as it is in your browser to generate a QR code for:

Example input:
$ https://github.com/ <return>

$ Enter the desired filename without the dot file extension. Example: my_qrcode.
$ (Hit return for 'QR_CODE' as a default):


Example Input:
$ myqrcode.png
$
$ ls
$ myqrcode.png


## Oddity in My System

My system was not either recognizing that qrcode was previously installed, or that pil_spec was.
So I added the following cludge.

```
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
...

```


If this thing doesn't happen for you, the script will run relatively faster if you comment this out. But it isn't slow enough to be botched with.


This explanation is 3x as long as the script.