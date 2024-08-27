import email.encoders
import os
import ssl
import smtplib
from dotenv import load_dotenv


### importamos las librerias para trabajar con el archivo adjunto
import email.mime.multipart
import email.mime.base
from email.mime.text import MIMEText

## para firmar el mensaje tengo que importar
from smail import sign_message


def enviarMail(email_receptor, asunto, cuerpo, rutaAdjunto):

    # Cargo las variables de entorno
    load_dotenv()

    email_emisor= os.getenv("EMAIL_EMISOR")
    email_contrasena=os.getenv("EMAIL_PASSWORD")
    servicio_smtp=os.getenv("SERVER_SMTP")
    port_smtp=os.getenv("PORT")
    cert_file = os.getenv("CERT_FILE_PATH")
    key_file = os.getenv("KEY_FILE_PATH")

    #aquí el mail al que le voy a enviar
    email_receptor = "fjimenezgestiones@gmail.com"

    #aquí los detalles del mail al que le voy a enviar. 
    asunto="Revisa tu correo con adjunto y con firma"
    cuerpo="""
    Este será el cuerpo del correo, 
    Que se puede poner en varios saltos de línea y darle el formato que queramos. 
    Además quiero informarte que el correo está firmado. 
    """

    ## aquí hago simple comprobación de que está cogiendo bien las variables de entorno. 
    print(email_emisor, email_contrasena, servicio_smtp, port_smtp)

    # aquí viene como se configura todo el mail. 
    em = email.mime.multipart.MIMEMultipart()
    em['From']=email_emisor
    em['To']=email_receptor
    em['Subject']=asunto

    ## añadimos el cuerpo del mail
    em.attach(MIMEText(cuerpo, 'plain'))

    # añadir el archivo adjunto que queremos especificando la ruta
    ruta_archivo_principal = 'pdfs/'
    ruta_archivo = ruta_archivo_principal + rutaAdjunto
    archivo = open(ruta_archivo, 'rb')
    adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunto.set_payload((archivo).read())
    email.encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', 'attachment; filename= %s' %rutaAdjunto)
    em.attach(adjunto)

    ## aquí procedemos a firmar el mail con la librería smail
    sign_mail = sign_message(em, key_file, cert_file)

    # tenemos que crear un contexto para luego pasarselo al smtplib.SMTP_SSL
    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL(servicio_smtp, port_smtp, context=contexto) as smtp:
        # Abrir la conexion y loguearnos con nuestro usuario y contraseña. 
        smtp.login(email_emisor, email_contrasena)
        
        # Enviar el mail sin firmar, dejo comentada esta línea
        ### smtp.sendmail(email_emisor, email_receptor, em.as_string())

        #Enviar mail firmado
        smtp.send_message(sign_mail)
        ### lamentablemente, despues de seguir todo, como la firma no está validada por ningún organismo válido
        ### Aun así, ya evito que el mail vaya a SPAM directamente o que incluso en el asunto me pongo [SPAM] como antes..., 
        ### según el tutorial seguido, se podría sustituir por una firma válida, por ejemplo de la fnmt (o tendré que buscar más info) 
        ### pero entonces me faltaría saber que tengo que poner en key_file y que poner en cert_file, ya que para la firma
        ### yo lo selecciono directamente desde windows siempre que quiero firmar algo....
        ### de momento lo dejo así. 


        # cerrar la conexion smtp
        smtp.quit()

    mensaje_exito = "Mail Enviado correctamente a " + email_receptor + " con adjunto: " + rutaAdjunto

    return mensaje_exito