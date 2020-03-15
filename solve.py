import pytesseract    
from pil import Image     

def main(file):
    #file = 'substinces.PNG'
    # opening an image from the source path 
    img = Image.open(file)
    dot = file.index(".")

    name = file[0:dot]

    # path where the tesseract module is installed 
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    # converts the image to result and saves it into result variable 
    result = pytesseract.image_to_string(img)    
    # write text in a text file and save it to source path    
    with open(name + '.txt',mode ='w') as file:      
        file.write(result)
        
    with open(name + '.txt',mode ='r') as file:      
        orig = file.read()
