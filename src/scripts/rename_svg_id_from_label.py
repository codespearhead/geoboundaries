import xml.etree.ElementTree as xmlParser
from unicodedata import normalize, combining
from os import listdir, makedirs
from os.path import join, exists

def remove_accents(input_str):
	nfkd_form = normalize('NFKD', input_str)
	return u"".join([c for c in nfkd_form if not combining(c)])

def snake_case(s):
	s = remove_accents(s).lower().strip()
	return '_'.join(s.split())

def save(svgData, path_to_output):
	svgData.write(path_to_output)


def rename(path_to_svg,
           path_to_output,
           labelName="{http://www.inkscape.org/namespaces/inkscape}label"):

	print("\n{}\n".format(path_to_svg))

	xmlDoc = xmlParser.parse(path_to_svg)
	rootElement = xmlDoc.getroot()
	for i, child in enumerate(rootElement):

		if (child.attrib.get("style", None)):
			child.attrib.pop("style")

		label = child.attrib.get(labelName, None)
		id = child.attrib.get("id", None)
		if (id is not None) and (label is not None):
			child.attrib["id"] = snake_case(label)
		
		label = child.attrib.get(labelName, None)
		id = child.attrib.get("id", None)
		print("[{}] id: {} - label: {}".format(i+1, id, label))
	
	save(xmlDoc, path_to_output)

def main(path_to_input_folder, path_to_output_folder):
	if not exists(path_to_output_folder):
		makedirs(path_to_output_folder)
	files = listdir(path_to_input_folder)
	for file in files:
		rename(
			join(path_to_input_folder, file),
			join(path_to_output_folder, file)
		)

main("src/maps/2", "src/maps/svg")