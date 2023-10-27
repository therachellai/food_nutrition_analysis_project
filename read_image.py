import tabula as tb
import pandas as pd
import os
from PIL import Image
import easyocr


def author():
    return 'Rachel Yu-Wei Lai'

###########################################################
def read_text(file_name: str):
    source_dir = 'INPUTS'
    file_name = 'foodlabel.png'
    reader = easyocr.Reader(['ch_sim','en'])
    text = reader.readtext(f'{source_dir}/{file_name}', detail = 0)
    print(text)
        
def convert_image_to_pdf():
    output_dir = 'OUTPUTS'
    source_dir = 'INPUTS'
    for file in os.listdir(source_dir):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
            image = Image.open(os.path.join(source_dir, file))
            image_converted = image.convert('RGB')
            image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))
    return

###########################################################
if __name__ == "__main__":
    convert_image_to_pdf()
    read_text('foodlabel.png')