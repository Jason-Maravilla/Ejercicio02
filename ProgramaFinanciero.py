class movimiento:
    def __init_(self):
        self.finanzaList =[]

    def realizarIngreso(self, montoIngreso):
        finanzaDict = {"TotalCuenta": 0.0}
        self.finanzaList.append(finanzaDict)
        for finanza in self.finanzaList:
            finanza["TotalCuenta"] += montoIngreso
    
    def hacerEgreso(self, montoEgreso):
        for finanza in self.finanzaList:
            finanza["TotalCuenta"] -= montoEgreso
    
    def obtenerSaldo(self):
        return self.finanzaList

class ingreso:
    def __init__(self):
        self.ingresosList = []
        self.idCounter = 0

    def realizarIngreso(self, idIngreso, montoIngreso):
        self.idCounter += 1
        idIngreso = self.idCounter
        finanzaDict ={"Total":0.0}
        ingresoDict = {"id": idIngreso, "monto": montoIngreso}
        self.ingresosList.append(ingresoDict)
        return ingresoDict
        
    def contarIngresos(self):
        for ingresos in self.ingresosList:
            return self.ingresosList


class egreso:
    def __init__(self):
        self.egresosList=[]
        self.idCounter =0

    def realizarEgreso(self, idEgreso, montoEgreso):
        self.idCounter += 1
        idEgreso= self.idCounter
        egresoDict = {"id": idEgreso, "monto": montoEgreso}
        self.egresosList.append(egresoDict)

    def contarEgresos(self):
        for egresos in self.egresosList:
            return self.egresosList