import xml.etree.ElementTree as xmlParser
import unicodedata

svg_file = "./Salinas-MG.svg"
svg_file_new = "a.svg"

xmlDoc = xmlParser.parse(svg_file)
rootElement = xmlDoc.getroot()
labelName = "{http://www.inkscape.org/namespaces/inkscape}label"

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def snake_case(s):
	s = remove_accents(s).lower().strip()
	return '_'.join(s.split())

for child in rootElement:
	label = child.attrib.get(labelName, None)
	id = child.attrib.get("id", None)
	if (id is not None) and (label is not None):
		child.attrib["id"] = snake_case(label)
		print(child.attrib.get("id", None))


# Saving the xml
# xmlDoc.write(svg_file_new)
