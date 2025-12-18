from PIL import Image
import os

def reducir_imagen(input_path, output_path, tamaño_objetivo_kb):
    # Cargar la imagen original
    img = Image.open(input_path)

    # Reducir calidad y tamaño iterativamente
    calidad = 95
    while calidad > 1:
        img.save(output_path, format='JPEG', quality=calidad)
        tamaño_actual_kb = os.path.getsize(output_path) / 1024
        if tamaño_actual_kb <= tamaño_objetivo_kb:
            break
        calidad -= 5  # Disminuir calidad

    print(f"Imagen optimizada a {tamaño_actual_kb:.2f} KB")

# Ejemplo de uso
reducir_imagen('C:\\Users\\ccaballerob\\Downloads\\foto Joshua.jpeg', 'C:\\Users\\ccaballerob\\Downloads\\foto Joshua2.jpeg', 100)