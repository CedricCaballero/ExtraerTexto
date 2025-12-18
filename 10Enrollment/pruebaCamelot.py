import camelot

# Cargar el PDF y extraer las tablas
tablas = camelot.read_pdf(r"file:///C:/Users/ccaballerob/Documents/Proyectos/10-validacion%20enrollment/documentos/Domicilio.pdf", pages="1")

# Mostrar cuántas tablas se encontraron
print(f"Se encontraron {tablas.n} tablas.")

# Exportar la primera tabla a CSV
tablas[0].to_csv("tabla1.csv")

# También puedes convertirla a DataFrame
df = tablas[0].df
print(df)
print(df[0][0])