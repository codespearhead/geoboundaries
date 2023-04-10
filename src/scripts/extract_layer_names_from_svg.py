import xml.etree.ElementTree as xmlParser
from os import listdir, makedirs
from os.path import join, exists


def save(layer_names, path_to_output):
	with open(join(path_to_output[:-4] + '.txt'), 'w') as f:
		for layer_name in layer_names:
			f.write(f"- {layer_name}\n")


def rename(path_to_svg,
           path_to_output,
           labelName="{http://www.inkscape.org/namespaces/inkscape}label"):

	print("\n{}\n".format(path_to_svg))

	xmlDoc = xmlParser.parse(path_to_svg)
	rootElement = xmlDoc.getroot()
	layer_names = []
	for i, child in enumerate(rootElement):
		label = child.attrib.get(labelName, None)
		if (label is not None):
			layer_names.append(label)
		print("[{}] - label: {}".format(i+1, label))

	save(layer_names, path_to_output)

def main(path_to_input_folder, path_to_output_folder):
	if not exists(path_to_output_folder):
		makedirs(path_to_output_folder)
	files = listdir(path_to_input_folder)
	for file in files:
		rename(
			join(path_to_input_folder, file),
			join(path_to_output_folder, file)
		)

main("src/maps/raw_svg", "src/maps/txt")