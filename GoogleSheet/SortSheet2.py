#Ordena mostrando en pantalla
import random
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de las credenciales de Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY_FILE = 'key.json'
SPREADSHEET_ID = '1LWltY6gJ9_320Bh-JUoB6I2i55V8JgBREd3qmfCPyPs'

creds = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

def initArray(size=10, maxValue=100, seed=3.14159):
    #Create an Array of the specified size with a fixed sequence of 'random' elements
    arr = [random.randrange(maxValue) for _ in range(size)]
    return arr

# Agregar números aleatorios en la columna A
numbers = initArray()

sheet.update('A2:A11', [[num] for num in numbers])


# Ordenar mediante BubbleSort y escribir en la columna C
arr = numbers.copy()
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            time.sleep(1)  # pausa de 1 segundos
            arr[j], arr[j+1] = arr[j+1], arr[j]
            sheet.update('C' + str(j+2), [[arr[j]]])  # actualizar la celda correspondiente
            sheet.update('C' + str(j+3), [[arr[j+1]]])  # actualizar la celda correspondiente
sheet.update('C2:C11', [[num] for num in arr])

# Ordenar mediante SelectionSort y escribir en la columna E
arr = numbers.copy()
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    time.sleep(1)  # pausa de 1 segundos
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    sheet.update('E' + str(i+2), [[arr[i]]])  # actualizar la celda correspondiente
    sheet.update('E' + str(min_idx+2), [[arr[min_idx]]])  # actualizar la celda correspondiente
sheet.update('E2:E11', [[num] for num in arr])

# Ordenar mediante InsertionSort y escribir en la columna G
arr = numbers.copy()
for i in range(1, len(arr)):
    key_item = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key_item:
        time.sleep(1)  # pausa de 1 segundos
        arr[j + 1] = arr[j]
        sheet.update('G' + str(j+3), [[arr[j]]])  # actualizar la celda correspondiente
        j -= 1
    arr[j + 1] = key_item
    sheet.update('G' + str(j+3), [[key_item]])  # actualizar la celda correspondiente
sheet.update('G2:G11', [[num] for num in arr])