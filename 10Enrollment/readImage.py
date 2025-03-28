import easyocr

class readImage:
    def __init__(self,image):
        self.image = image
        self.results = None
        self.reader = easyocr.Reader(['es'],gpu=True)
    #Analiza la imagen
    def read_Image(self):
        self.results = self.reader.readtext(self.image)
        #print(results)
        #exit()
        return self.results