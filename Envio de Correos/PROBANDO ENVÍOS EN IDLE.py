#Nombre: Nicolás Alberto Graza Galicia
#Matricula: 1998776

import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('alfperez3@gmail.com','jsmf ccak daiu cynu')
conn.sendmail('alfperez3@gmail.com','aaron28perez@gmail.com','Subject: TestPractica10\n\nHola\n\n Prueba de 1993809- Aaron Perez Esparza' )
conn.quit()