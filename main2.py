from enviarMail import enviarMail
from ExcelModel import crearExcel, escribirPathsAdjuntos, getListaEnvio, ponerComoEnviados
from ExcelModel import cerrarExcel, isExcelAbierto

#crearExcel()

#escribirPathsAdjuntos()

if isExcelAbierto():
    cerrarExcel()

listaCorreos = getListaEnvio()

listaIdEnviados = []

for correo in listaCorreos:
    if correo[6] != "Enviado":
        # enviarMail(correo[2], correo[3],correo[4],correo[5])
        print("Enviado correctamente: ", correo[2], correo[3],correo[5])
        listaIdEnviados.append(correo[0])

ponerComoEnviados(listaIdEnviados)


