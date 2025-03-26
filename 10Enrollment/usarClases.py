from rectanguloINE import RecortarINE
import cv2

ine = RecortarINE(r"C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\imagenS\ine_page_1.png")
recortes = ine.Recorta()
print(len(recortes))
for img in recortes:
    cv2.imshow(f'Recorte ', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
