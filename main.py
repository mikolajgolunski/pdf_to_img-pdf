import sys
import tempfile
from glob import glob
import os
from pdf2image import convert_from_path


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def find_ext(directory, extension, ignore_case=True):
    if ignore_case:
        extension = "".join(["[{}]".format(char + char.swapcase()) for char in extension])
    return glob(os.path.join(directory, "*." + extension))


if __name__ == '__main__':
    application_path = os.path.dirname(sys.executable)
    real_poppler_path = resource_path(r'.\poppler')
    print('Finding all pdfs in the folder')
    pdfs = find_ext(application_path, 'pdf')
    for pdf_nr, pdf in enumerate(pdfs):
        path, filename = os.path.split(pdf)
        filename = os.path.splitext(filename)[0]
        output_filename = 'converted_%s.pdf' % filename
        output_path = os.path.join(path, output_filename)
        print('-'*10)
        print('Converting file nr ' + str(pdf_nr+1) + ' : ' + filename)
        with tempfile.TemporaryDirectory() as path:
            print('Extracting pages')
            images_from_path = convert_from_path(pdf, output_folder=path, poppler_path=real_poppler_path)
            print('Combining pages to one pdf')
            if len(images_from_path) > 1:
                images_from_path[0].save(output_path, save_all=True, append_images=images_from_path[1:])
            else:
                images_from_path[0].save(output_path)
    print('-'*10)
    print('Finished')

