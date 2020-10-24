from ProgramaFinanciero import movimiento
from ProgramaFinanciero import ingreso
from ProgramaFinanciero import egreso

print("Inicio Movimiento, Ingresos y Egresos: \n")
movimientoObj= movimiento()
ingresosObj = ingreso()
egresosObj = egreso()

def ponerDinero():
   print("**Realizar un nuevo ingreso**")
   montoIngreso = float(input("Monto: "))
   ingresosObj.realizarIngreso(montoIngreso)
   movimientoObj.realizarIngreso(montoIngreso)
    
def quitarDinero():
    print("**realizar un nuevo egreso")
    montoEgreso = float(input("Monto: "))
    egresosObj.realizarEgreso(montoEgreso)
    movimientoObj.hacerEgreso(montoEgreso)

def obtenerSaldo():
    finanzaList = movimientoObj.obtenerSaldo()
    for finanza in finanzaList:
        print(finanza)

def obtenerIngresos():
    finanzaList = ingresosObj.contarIngresos() 
    for ingresos in finanzaList:
        print(ingresos)  

def obtenerEgresos():
    egresosList = egresosObj.contarEgresos()
    for egresos in egresosList:
        print(egresos)     

def obtenerMovimientos():
    cantidadIngresos = ingresosObj.contarIngresos()
    cantidadEgresos = egresosObj.contarEgresos()
    if (cantidadIngresos ==0) and (cantidadEgresos ==0):
        print("No se ha realizado ningún tipo de transaccion")
    else:
        print("**Aqui esta su reporte personal de transacciones**")
        obtenerIngresos()
        obtenerEgresos()

while True:
    print("Menu: \n") 
    print("Presione:")
    print("(0) Para salir")
    print("(1) Mostrar el saldo total de la cuenta")
    print("(2) Realizar un ingreso")
    print("(3) Realizar un egreso")
    print("(4) Ver el historial de Ingresos")
    print("(5) Ver historial de Egresos")
    print("(6) Ver reporte completo de movimientos \n")
    option = int(input("opcion: "))

    if option == 0:
        print("termino el programa\n")
        break
    elif option == 1:
        obtenerSaldo()
    elif option == 2:
        ponerDinero()
    elif option == 3:
        quitarDinero()
    elif option == 4:
        obtenerIngresos()
    elif option == 5:
        obtenerEgresos()
    elif option == 6:
        obtenerMovimientos()  
       

        






