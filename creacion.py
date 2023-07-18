# https://www.youtube.com/watch?v=A1URtaaA-v0
#tutorial Python y Hojas de calculo de Google Drive 

import gspread

gc = gspread.service_account(filename='conexionsheetspython-392422-0a820babdddc.json')

# Crear nuevo archivo
sh = gc.create('NuevoProy')

#En este caso debo dar permisos a mi google drive principal
sh.share('ingparismendi@gmail.com', perm_type='user', role='writer')

# Abrir por titulo
sh = gc.open('NuevoProy')

# Seleccionar primera hoja
worksheet = sh.get_worksheet(0)

#Introducir datos
worksheet.update('A1', 'Dominio')
worksheet.update('A2', 'Scraping.link')
worksheet.update('B1', 'Fecha')
worksheet.update('B2', '22/04/2021')
worksheet.update('C1', 'Num URL indexados')
worksheet.update('C2', '10')

