import easyocr

def initialize_ocr():
    return easyocr.Reader(['en'])

def read_text(reader, file_path):
    results = reader.readtext(file_path)
    return ' '.join([result[1] for result in results])