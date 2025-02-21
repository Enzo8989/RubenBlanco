from Google import Create_Service

CLIENT_SECRET_FILE = "credOA.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

ID_calendario = "treasurerealgold@gmail.com"

def anadirCita(nombre,email,telefono,fecha,hora,hora_fin):
    evento = {
        'summary': f'Cita con {nombre}',
        'description': f'Cliente: {nombre}\nTeléfono: {telefono}',
        'start':{
            'dateTime': f'{fecha}T{hora}',
            'timeZone': 'Europe/Madrid',
        },
        'end':{
            'dateTime': f'{fecha}T{hora_fin}',
            'timeZone': 'Europe/Madrid',
        },
        'attendees':[{
            'email':email
        },],
    }

    service.events().insert(calendarID = "primary", body = evento).execute()