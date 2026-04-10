import zipfile
import xml.etree.ElementTree as ET

def extract_docx(file_path):
    with zipfile.ZipFile(file_path) as z:
        root = ET.fromstring(z.read('word/document.xml'))
        text = '\n'.join(''.join(node.itertext()) for node in root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
        return text

if __name__ == '__main__':
    text = extract_docx('SSB_Analisis_OnBoarding.docx')
    with open('ssb_extracted.txt', 'w', encoding='utf-8') as f:
        f.write(text)
