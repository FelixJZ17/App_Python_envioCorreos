import email.encoders
import os
import ssl
import smtplib
from dotenv import load_dotenv

### importamos las librerias para trabajar con el archivo adjunto
import email.mime.multipart
import email.mime.base
from email.mime.text import MIMEText

# Cargo las variables de entorno
load_dotenv()

email_emisor= os.getenv("EMAIL_EMISOR")
email_contrasena=os.getenv("EMAIL_PASSWORD")
servicio_smtp=os.getenv("SERVER_SMTP")
port_smtp=os.getenv("PORT")


#aquí el mail al que le voy a enviar
email_receptor = "ejemplo@ejemplo.com"

#aquí los detalles del mail al que le voy a enviar. 
asunto="Revisa tu correo con adjunto"
cuerpo="""
Este será el cuerpo del correo, 
Que se puede poner en varios saltos de línea y darle el formato que queramos. 
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
ruta_archivo = '/pdfs/ejemplo.pdf'
archivo = open(ruta_archivo, 'rb')
adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
adjunto.set_payload((archivo).read())
email.encoders.encode_base64(adjunto)
adjunto.add_header('Content-Disposition', 'attachment; filename= %s' %ruta_archivo)
em.attach(adjunto)

# tenemos que crear un contexto para luego pasarselo al smtplib.SMTP_SSL
contexto = ssl.create_default_context()

with smtplib.SMTP_SSL(servicio_smtp, port_smtp, context=contexto) as smtp:
    # Abrir la conexion y loguearnos con nuestro usuario y contraseña. 
    smtp.login(email_emisor, email_contrasena)
    # Enviar el mail
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
    # cerrar la conexion smtp
    smtp.quit()



