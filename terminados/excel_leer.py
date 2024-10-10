import openpyxl

def leer_excel(Excel_Leer_Escribir):
    wb = openpyxl.load_workbook(Excel_Leer_Escribir)
    sheet = wb.active
    dato1 = sheet['A2'].value
    dato2 = sheet['B2'].value
    dato3 = sheet['B3'].value
    dato4 = sheet['B4'].value
    print(u'-----------------------------------------')
    print(u'El libro de excel utilizado es; ' + Excel_Leer_Escribir)
    print(u'El valor de la celda es: '+ dato1)
    print(u'El valor de la celda es: '+ dato2)
    print(u'El valor de la celda es: '+ dato3)
    print(u'El valor de la celda es: '+ dato4)
    print(u'-----------------------------------------')
    return dato1, dato2, dato3, dato4

        
