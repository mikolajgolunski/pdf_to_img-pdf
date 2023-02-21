# pdf to img-pdf

Converting pdfs into pdfs consisting of images of pages from original pdfs.

Script finds all pdfs in the folder it is in and converts each of them individually outputting pdf with "converted_" added in front of its name. Each pdf is converted page by page using pdf2img to PIL images and then saved again as pdf with PIL method.

It can be used to disallow recipient copying text from your pdf.

File is prepared to be compiled into executable using PyInstaller. It requires poppler to be downloaded and placed in "poppler" folder. I used version from https://github.com/oschwartz10612/poppler-windows/releases/ that was given in the PyPI pdf2img site https://pypi.org/project/pdf2img/

Hooks folder can be also linked during PyInstaller process as additional hooks directory.