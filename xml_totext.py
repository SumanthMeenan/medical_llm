import xml.etree.ElementTree as ET

# Function to parse XML and extract text content recursively
def extract_text_from_xml(element):
    text = element.text or ''
    for child in element:
        text += extract_text_from_xml(child)
    return text

# Input XML file path
xml_file_path = 'data.xml'

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Extract text content from XML
text_content = extract_text_from_xml(root)

# Remove empty lines and lines with only spaces from the text content
text_content = '\n'.join(line.strip() for line in text_content.splitlines() if line.strip())

# Output text file path
text_file_path = 'output.txt'

# Write the extracted text content to a text file
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(text_content)

print(f'Text content extracted from XML, empty lines and lines with only spaces removed, and saved to {text_file_path}')
