pip install qrcode



import qrcode
img = qrcode.make("https://www.youtube.com/c/swetaverma")
img.save("youtube.jpg")

