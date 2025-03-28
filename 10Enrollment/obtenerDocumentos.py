import os
import glob

class Documentos:
    def __init__(self, pathFile):
        self.pathFile = pathFile

    #**************Lista los archivos de la ruta *****************
    def listar_archivos(self):
        ruta = self.pathFile
        # Patrones para archivos PDF e imágenes
        patrones = ["*.pdf", "*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tiff"]
        archivos = []
        for patron in patrones:
            archivos2 = glob.glob(os.path.join(ruta, patron))
            for archivo in archivos2:
                extension = os.path.splitext(archivo)[1].lower()
                nombre = os.path.splitext(os.path.basename(archivo))[0]
                if extension == ".pdf":
                    tipo = "PDF"
                elif extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]:
                    tipo = "Imagen"
                archivos.append((archivo, tipo,nombre))
        return archivos