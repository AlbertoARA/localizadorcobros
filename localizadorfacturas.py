import xlrd
from itertools import combinations

loc = ("movimientosfiltrado.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)
print(sheet.ncols)
print(sheet.nrows)
print("")

clientes = []
importe = []

coincidencias = []
listadofacturas = []


for i in range(sheet.nrows):
   clientes.append(sheet.cell_value(i,1))
   importe.append(sheet.cell_value(i,2))



def localizarfactura():
    masfactura = 1
    while masfactura == 1:
        factura = float(input("Introduce importe de factura a localizar: "))
        print("")
        listadofacturas.append(factura)
        masfactura = int(input("hay mas facturas de este cliente en fechas aproximadas? (pulse 1 para sí, 0 para no): "))
        print("")
        largolistado = len(listadofacturas)
        print(largolistado)
    for i in range(1,largolistado+1):
        combina = list(combinations(listadofacturas,i))
        suma = 0.0
        if i == 1:
            suma = 0.0
            for j in range(len(combina)):
                aux = combina[j][0]
                print("aux",aux)
                suma = aux

                if suma in importe:
                    posicion = importe.index(suma)
                    print("aqui esta,",sheet.cell_value(posicion,0),sheet.cell_value(posicion,1),sheet.cell_value(posicion,2))
                    print("combina j",combina[j],"suma",suma)
                    print("")
                    coincidencias.append(suma)
                    suma = 0.0
                else:
                    print("no hay ninguna factura que coincida")
                    print("combina j",combina[j],"suma",suma)
                    print("")
                    suma = 0.0

        else:
            suma = 0.0
            for j in range(len(combina)):
                for r in range (i):
                    aux = combina[j][r]
                    print("aux",aux)
                    suma += aux
                    suma = round(suma,2)

                if suma in importe:
                    posicion = importe.index(suma)
                    print("aqui esta,",sheet.cell_value(posicion,0),sheet.cell_value(posicion,1),sheet.cell_value(posicion,2))
                    print("combina j",combina[j],"suma",suma)
                    print("")
                    coincidencias.append(suma)
                    suma = 0.0
                else:
                    print("no hay ninguna factura que coincida")
                    print("combina j",combina[j],"suma",suma)
                    print("")
                    suma = 0.0


def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            print("")
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Localizar pago")
    print ("2. Impagados")
    print ("3. Ver ingresos")
    print ("4. Salir")
     
    print ("Elige una opcion")
    print("")
    print("")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        localizarfactura()
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 

print(coincidencias)
print ("Fin")
