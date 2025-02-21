from Google import Create_Service

# Configuración
CLIENT_SECRET_FILE = "credOA.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

ID_calendario = "treasurerealgold@gmail.com"
page_token = None
while True:
  calendar_list = service.calendarList().list(calendarId='primary', pageToken=page_token).execute()
  for calendar_list_entry in calendar_list['items']:
    print (calendar_list_entry['summary'])
  page_token = calendar_list.get('nextPageToken')
  if not page_token:
    break