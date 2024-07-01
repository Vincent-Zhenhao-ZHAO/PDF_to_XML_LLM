import PyPDF2
import xml.etree.ElementTree as ET

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = []
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return text

# def 

# def create_xml(data, output_file):
#     root = ET.Element('Root')
#     for item in data:
#         entry = ET.SubElement(root, 'Entry')
#         for key, value in item.items():
#             child = ET.SubElement(entry, key)
#             child.text = str(value)
    
#     tree = ET.ElementTree(root)
#     tree.write(output_file)

text = extract_text_from_pdf('paper_for_test/1-s2.0-S0010482521008313-main.pdf')

# output file
with open('output.txt', 'w') as file:
    for page in text:
        file.write(page)
        file.write('\n')
    file.close()

print('Text extracted from PDF and saved to output.txt')

