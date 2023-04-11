from os import listdir, makedirs
from os.path import join, exists
from subprocess import call


def inkscape_svg_to_plain_svg(path_to_svg, path_to_output):
    print('\n{}\n{}'.format(path_to_svg, path_to_output))
    call(['inkscape',
          f'{path_to_svg}',
          '--export-plain-svg',
          '--export-type=svg',
          f'--export-filename={path_to_output}'])


def main(path_to_input_folder, path_to_output_folder):
    if not exists(path_to_output_folder):
        makedirs(path_to_output_folder)
    files = listdir(path_to_input_folder)
    for file in files:
        inkscape_svg_to_plain_svg(
            join(path_to_input_folder, file),
            join(path_to_output_folder, file)
        )


main("src/maps/svg", "src/maps/raw_svg")