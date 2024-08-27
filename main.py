import ssl
from email.message import EmailMessage
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_emisor= os.getenv("EMAIL_EMISOR")
email_contrasena=os.getenv("EMAIL_PASSWORD")
servicio_smtp=os.getenv("SERVER_SMTP")
port_smtp=os.getenv("PORT")

email_receptor = "ejemplo@ejemplo.com"

asunto="Revisa tu correo"
cuerpo="""
Este será el cuerpo del correo, 
Que se puede poner en varios saltos de línea y darle el formato que queramos. 
"""

## aquí hago simple comprobación de que está cogiendo bien las variables de entorno. 
print(email_emisor, email_contrasena, servicio_smtp, port_smtp)

em = EmailMessage()
em['From']=email_emisor
em['To']=email_receptor
em['Subject']=asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL(servicio_smtp, port_smtp, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())

    

