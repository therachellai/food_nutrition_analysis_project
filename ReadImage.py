import tabula as tb
import pandas as pd
import os
from PIL import Image
import easyocr


def author():
    return 'Rachel Yu-Wei Lai'

###########################################################
def read_text(file_name: str):
    """
    This function uses easyocr, and OCR framework to read text from a file, given the 
    file name.
    ------------------
    Parameters: 
    file_name: file name in str, currently called foodlabel.png, subject to future changes
    ------------------
    Returns: text in str
    """
    source_dir = 'INPUTS'
    file_name = 'foodlabel.png'
    reader = easyocr.Reader(['ch_sim','en'])
    text = reader.readtext(f'{source_dir}/{file_name}', detail = 0)
    print(text)
    return text
        
def convert_image_to_pdf():
    """
    This function converts all png, jpg, or jpeg images files to PDF for better processing 
    in the future.
    ------------------
    Parameters: None
    ------------------
    Returns: None
    """
    output_dir = 'OUTPUTS'
    source_dir = 'INPUTS'
    for file in os.listdir(source_dir):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
            image = Image.open(os.path.join(source_dir, file))
            image_converted = image.convert('RGB')
            image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))
    return

def extract_info_from_string(text: str):
    """Using the text output from read_text function, extract info and convert it into a 
    pandas df. Each time we run the read_text function, the output will become one row in 
    the final df. The idea is to get ~200 entries/rows (aka food items) in our database. 
    Maybe store the data in AWS or snowflake? Let me know what you guys think.
    
    Args:
        text (str): _description_
    """
    pass

###########################################################
if __name__ == "__main__":
    # convert_image_to_pdf()
    text = read_text('foodlabel.png')
    extract_info_from_string(text)