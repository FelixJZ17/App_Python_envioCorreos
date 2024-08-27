import os
from openpyxl import Workbook

def crearExcel():
    
    if comprobarSiExiste():
        print("El archivo de excel ya existe, por favor, borralo para crearlo desde cero")
    else:
        # Crear un nuevo libro de trabajo
        workbook = Workbook()
        # Seleccionar la hoja activa
        sheet = workbook.active
        
        # Especificar los encabezados
        encabezados = ["id", "nombre", "mail", "asunto", "cuerpo_mensaje", "path_adjunto", "estado_mail", "fecha_envio"]
        
        # Asignar los encabezados en la fila 1
        sheet.append(encabezados)
        
        # Guardar el archivo Excel en el directorio actual con el nombre "datos_mensajes.xlsx"
        workbook.save("datos_mensajes.xlsx")

def comprobarSiExiste():
    # Verificar si el archivo "datos_mensajes.xlsx" existe en el directorio actual
    return os.path.isfile("datos_mensajes.xlsx")