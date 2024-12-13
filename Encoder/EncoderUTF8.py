def EncodingUTF8(string):
    encoding = fr"{string}"
    encoded = encoding.encode('utf-8')
    return encoded