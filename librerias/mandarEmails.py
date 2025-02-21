from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = "credOA.json"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://www.mail.google.com/"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def enviarMail(nombre,email,telefono,fecha,hora):
    emailMsg = f'Confirmación  de cita \n\n Cliente: {nombre} \n Teléfono : {telefono} \n Cita : {fecha} a la {hora} \n\n En caso de No poder asistir responda este correo, gracias \n\n Un saludo'
    mimeMessage = MIMEMultipart()
    mimeMessage["to"] = email
    mimeMessage["subject"] = f'{nombre} esta su confirmación de la cita'
    mimeMessage.attach(MIMEText(emailMsg,"plain"))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    service.users().messages().send(userId = "me",body = {"raw":raw_string}).execute()



    








    

    

