
import smtplib, ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Correo del remitente: ")
receiver_email = input("Correo destinatario: ")
password = getpass.getpass("Password del remitente: ")

#Se analizan los mensajes que se enviarán en el asunto del correo
message = MIMEMultipart("alternative")
message["Subject"] = "Prueba de envio (script Python) - 1998776"
message["From"] = sender_email
message["To"] = receiver_email

#Escribimos el mensaje en formato HTML
html = """\
<html>
  <body>
    
    <p><strong> <h2> Practica 12 </h2> </strong> <br>
       Ejercicio de la practica 12 para envío de correos<br> 
       <strong> Alumno: </strong> Nicolas Alberto Garza Galicia <br>
       <strong> Matricula: </strong>  1998776
    </p>
  </body>
</html>
"""
#Anexamos al correo la parte del HTML
parte_html = MIMEText(html, 'html')
message.attach(parte_html)

#Se agregará la imagen de fcfm_cool.png
archivo = 'fcfm_cool.png'

#Abrimos el archivo
with open(archivo, 'rb') as adjunto:
    contenido_adjunto = MIMEBase('application','octet-stream')
    contenido_adjunto.set_payload(adjunto.read())
encoders.encode_base64(contenido_adjunto)
contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {archivo}"
)

#Se agrega todo lo anterior al mensaje a enviar
message.attach(contenido_adjunto)
mensaje_final = message.as_string()

#Establecemos conexión con smtp
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

#Nombre: Nicolás Alberto Gaarza Galicia
#Matricula: 1998776
