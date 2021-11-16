from binascii import a2b_base64

data = '''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'''
binary_data = a2b_base64(data)

fd = open('image.png', 'wb')
fd.write(binary_data)
fd.close()
