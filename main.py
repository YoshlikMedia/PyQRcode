import pyqrcode

text = pyqrcode.create('https://t.me/DeCoder_uz')

text.png('qrcode.png', scale=5)

print(text.terminal('white', 'blue'))

