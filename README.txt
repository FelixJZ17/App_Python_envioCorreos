Este programa inicia en el main.py, que junto con una Excel complementaria, que tendrá 5 columnas, hará lo siguiente: 

del excel
- La columna 1-A - contendrá el nombre del receptor del mail. 
- La columna 2-B - tendrá el mail de envío. 
- La columna 3-C - La tercera tendrá el asunto del mail. 
- La columna 4-D - Tendrá el cuerpo del mail. 
- La columna 5-E - Tendrá la ruta que dirige al adjunto para adjuntarlo en el correo. 

-----------------

Además de todo esto, creamos un documento Python, que no se subirá a GitHub, con las variables de entorno para poder loguearnos en nuestro servidor de correo y hacer el envío SMTP.
# el nombre del archivo en la carpeta raiz debe ser ---> .env
EMAIL_PASSWORD="" # ejemplo: contraseña_ejemplo
EMAIL_EMISOR=""  #ejemplo: hola_ejemplo@gmail.com
SERVER_SMTP=""   # ejemplo: "smtp.gmail.com"
PORT=465          ### --> para SSL se usa el 465, para el TLS se usa el 587 