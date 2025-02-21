import gspread
from google.oauth2.service_account import Credentials

clave = 'credSA.json'
objetivo = ['https://www.googleapis.com/auth/spreadsheets']
archivo_ID = '1ze2rofI8W9S9OLb_9FfATiCTLgwR9bA4T3RSgrWz2Rc'

credenciales = Credentials.from_service_account_file(
    clave,scopes=objetivo)
servicio  = gspread.authorize(credenciales)
acceso = servicio.open_by_key(archivo_ID)

def grabarSheets(nombre,email,telefono,fecha,hora,hora_fin):
    hoja = acceso.worksheet('p1')

    nueva_fila = [nombre,email,telefono,fecha,hora,hora_fin]
    hoja.append_row(nueva_fila)
