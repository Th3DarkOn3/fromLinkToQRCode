import qrcode
import os

def get_os():
    return os.name

url = input("Enter the link or test to convert to QR: ")
path = input("Enter the path where the qrcode will be saved : ")
if get_os() == 'nt':
    if path[len(path) - 1] == "\\":
        path+= "qrcode.png"
    else:
        path+= "\qrcode.png"
else:
    if path[len(path) - 1] == "/":
        path+= "qrcode.png"
    else:
        path+= "/qrcode.png"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make()

# Save the QR code to a file
qr_image = qr.make_image()
qr_image.save(path)
