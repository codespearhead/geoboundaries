import xml.etree.ElementTree as xmlParser
from os import listdir, makedirs
from os.path import join, exists, isfile


def reorder_attributes(root):
	for el in root.iter():
		attrib = el.attrib
		if len(attrib) > 1:
			attribs = sorted(attrib.items())
			attrib.clear()
			attrib.update(attribs)


def save(svgData, path_to_output):
	svgData.write(path_to_output)


def rename(path_to_svg,
           path_to_output,
           current_tag_name="{http://www.inkscape.org/namespaces/inkscape}label",
		   new_tag_name="data-name"):

	print("\n{}\n".format(path_to_svg))

	xmlDoc = xmlParser.parse(path_to_svg)
	rootElement = xmlDoc.getroot()
	for i, child in enumerate(rootElement):
		
		current_tag_value = child.attrib.get(current_tag_name, None)

		if (child.attrib.get("style", None)):
			child.attrib.pop("style")

		if (current_tag_value is not None and child.tag == "path"):
			child.attrib[new_tag_name] = current_tag_value
			child.attrib.pop(current_tag_name)

			child.attrib['class'] = 'neighborhood'
		reorder_attributes(child)
		
		new_tag_value = child.attrib.get(new_tag_name, None)
		print(f"[{i+1}] {new_tag_name}: {new_tag_value} - {current_tag_name}: {current_tag_value}")
	save(xmlDoc, path_to_output)


def main(path_to_input_folder, path_to_output_folder):
	files = [ f for f in listdir(path_to_input_folder) if isfile(join(path_to_input_folder, f)) ]
	if not exists(path_to_output_folder):
		makedirs(path_to_output_folder)
	for file in files:
		rename(
			join(path_to_input_folder, file),
			join(path_to_output_folder, file)
		)


main("src/maps/1", "src/maps/2")