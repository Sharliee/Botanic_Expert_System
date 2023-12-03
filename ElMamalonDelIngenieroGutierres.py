"""

Nombre:      Carlos Andres Riveramelo Del Toro
Materia:     Sistemas Expertos
Docente:     Mauricio Alejandro Cabrera Arellano

"Sistema Experto En Plantas (El Mamalon Del Ingeniero Gutierrez)"

"""

import sys

#################### Modulo del ingeniero ####################

def ingeniero():
        PlantasT=['Arboles',
                 'Plantas Suculentas',
                 'Plantas Trepadoras',
                 'Epifitas y Hemiepifitas',
                 'Parasitas',
                 'Saprofitas',
                 'Higuerones',
                 'Helechos',
                 'Hepaticas',
                 'Plantas Insectivoras']
        
        print ('Modo Ingeniero')
        print ('Adquisicion de Nuevo Conocimiento sobre Plantas')
        
        nombre = input('Introduce el Nombre de la planta: ')
        colorhojas = input('Introduce el color de las hojas de %s: ' %(nombre))
        colortallo = input('Introduce el color de el tallo de %s: '%(nombre))
        tammin = input('Introduce el tamaño minimo de %s: '%(nombre))
        tammax = input('Introduce el tamaño maximo de %s: '%(nombre))
        zona = input('Introduce la zona donde crece %s: '%(nombre))
        
        print ('elije un tipo de planta: ')
        print ('01.- Arboles')
        print ('02.- Plantas Suculentas')
        print ('03.- Plantas Trepadoras')
        print ('04.- Epifitas y Hemiepifitas')
        print ('05.- Parasitas')
        print ('06.- Saprofitas')
        print ('07.- Higuerones')
        print ('08.- Helechos')
        print ('09.- Hepaticas')
        print ('10.- Plantas Insectivoras')
        
        tipo = input('Introduce el tipo de planta al que pertenece %s: '%(nombre))
        file = open('conocimiento','a')
        file.write('\n')
        file.write(nombre+'|'+str(colorhojas)+'|'+str(colortallo)+'|'+str(tammin)+'|'+str(tammax)+'|'+str(zona)+'|'+PlantasT[int(tipo)-1])
        file.close()
        
################### Modulo del conocimiento ##################

class Plant(object):
        def __init__(self, nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo):
                super(Plant, self).__init__()
                self.nombre = nombre
                self.colorhojas = colorhojas
                self.colortallo = colortallo
                self.tammin = tammin
                self.tammax = tammax
                self.clima = clima
                self.zona = zona
                self.tipo = tipo
        
        def mostrarPlanta(self):
                print ("%s %s %s %s %s %s %s %s" %(self.nombre, self.colorhojas, self.colortallo, self.tammin, self.tammax, self.clima, self.zona, self.tipo))
Plants=[]

class NewPlant(object):
        def __init__(self, nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo):
                super(NewPlant, self).__init__()
                self.nombre = nombre
                self.colorhojas = colorhojas
                self.colortallo = colortallo
                self.tammin = tammin
                self.tammax = tammax
                self.clima = clima
                self.zona = zona
                self.tipo = tipo
newplant=[]
        
def cargaConocimientoPlantas():
        n = 0
        file = open('conocimiento','r')
        while True:
                pass
                n = n+1
                linea = file.readline()
                if not linea: break
                plnt = linea.split('|')
                Plants.append(Plant(plnt[0], plnt[1], plnt[2], plnt[3], plnt[4], plnt[5], plnt[6], plnt[7]))
cargaConocimientoPlantas()

def cargaConocimientoNewPlants():
        file = open ('Perfiles','r')
        while True:
                pass
                linea = file.readline()
                if not linea: break
                per = linea.split('|')
                newplant.append(NewPlant(per[0], per[1], per[2], per[3], per[4], per[5], per[6], per[7]))
cargaConocimientoNewPlants()

def OAV():
        OAV = open('OAV','w')
        file = open('conocimiento','r')
        while True:
                pass
                linea = file.readline()
                if not linea: break
                plnt = linea.split('|')
                OAV.write ('Objeto         Atributo         Valor')
                OAV.write ('\n')
                OAV.write ('\nPlanta     Nombre               '+plnt[0])
                OAV.write ('\nPlanta     Color de Hojas       '+plnt[1])
                OAV.write ('\nPlanta     Color de Tallo       '+plnt[2])
                OAV.write ('\nPlanta     Tamaño Minimo        '+plnt[3])
                OAV.write ('\nPlanta     Tamaño Maximo        '+plnt[4])
                OAV.write ('\nPlanta     Clima                '+plnt[5])
                OAV.write ('\nPlanta     Zona                 '+plnt[6])
                OAV.write ('\nPlanta     Tipo                 '+plnt[7])
                OAV.write ('\n\n\n')
        OAV.close()
        file.close()
OAV()
def Recordar(nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo):
        file = open('Perfiles','a')
        file.write('\n')
        file.write(str(nombre)+'|'+str(colorhojas)+'|'+str(colortallo)+'|'+str(tammin)+'|'+str(tammax)+'|'+str(clima)+'|'+str(zona)+'|'+str(tipo))
        file.close()
        
def Recordar2(nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo):
        file = open('conocimiento','a')
        file.write('\n')
        file.write(str(nombre)+'|'+str(colorhojas)+'|'+str(colortallo)+'|'+str(tammin)+'|'+str(tammax)+'|'+str(clima)+'|'+str(zona)+'|'+str(tipo))
        file.close()

"Modulo de inferencia"

def Desconocido(nombre):
        for x in range(len(newplant)):
                pass
                if (nombre == newplant[x].nombre):
                        return newplant[x]
                elif (x == len(newplant) and nombre != newplant[x].nombre):
                        return False
                    
def planta(cuidados):
        
        Arboles_1 = []
        Plantas_Suculentas = []
        Plantas_Trepadoras = []
        Epifitas_Hemiepifitas = []
        Parasitas_1 = []
        Saprofitas_1 = []
        Higuerones_1 = []
        Helechos_1 = []
        Hepaticas_1 = []
        Plantas_Insectivoras = []
        
        for x in range(len(Plants)):
                pass
                if ('Arboles' in Plants[x].tipo):
                        pass
                        Arboles_1.append(Plants[x])
                if ('Plantas Suculentas' in Plants[x].tipo):
                        pass
                        Plantas_Suculentas.append(Plants[x])
                if ('Plantas Trepadoras' in Plants[x].tipo):
                        pass
                        Plantas_Trepadoras.append(Plants[x])
                if ('Epifitas y Hemiepifitas' in Plants[x].tipo):
                        pass
                        Epifitas_Hemiepifitas.append(Plants[x])
                
                if ('Parasitas' in Plants[x].tipo):
                        pass
                        Parasitas_1.append(Plants[x])
                if ('Saprofitas' in Plants[x].tipo):
                        pass
                        Saprofitas_1.append(Plants[x])
                if ('Higuerones' in Plants[x].tipo):
                        pass
                        Higuerones_1.append(Plants[x])
                if ('Helechos' in Plants[x].tipo):
                        pass
                        Helechos_1.append(Plants[x])
                if ('Hepaticas' in Plants[x].tipo):
                        pass
                        Hepaticas_1.append(Plants[x])
                if ('Plantas Insectivoras' in Plants[x].tipo):
                        pass
                        Plantas_Insectivoras.append(Plants[x])
                
                if (cuidados == 'cArboles'):
                        return Arboles_1
                elif (cuidados == 'cPlantas Suculentas'):
                        return Plantas_Suculentas
                elif (cuidados == 'cPlantas Trepadoras'):
                        return Plantas_Trepadoras
                elif (cuidados == 'cEpifitas y Hemiepifitas'):
                        return Epifitas_Hemiepifitas
                elif (cuidados == 'cParasitas'):
                        return Parasitas_1
                elif (cuidados == 'cSaprofitas'):
                        return Saprofitas_1
                elif (cuidados == 'cHiguerones'):
                        return Higuerones_1
                elif (cuidados == 'cHelechos'):
                        return Helechos_1
                elif (cuidados == 'cHepaticas'):
                        return Hepaticas_1
                elif (cuidados == 'cPlantas Insectivo'):
                        return Plantas_Insectivoras

def main():
        print ('\n\n\n')
        print ("                    BOTANIC EXPERT SYSTEM")
        print ('\n\n\n')
        print ("Para agregar o consultar una planta favor de contestar lo siguiente...")
        print ('\n')
        
        nombre = input('Cual es el nombre de la planta: ')
        conosco = Desconocido(nombre)
        
        if (conosco):
                print ('\n')
                print ('¡%s esta registrada!'%(conosco.nombre))
                print ('\n')
                print ('Nombre:             %s\nColor de hoja:      %s\nColor de tallo:     %s\nTamaño minimo:      %s\nTamaño maximo:      %s\nClima:              %s\nZona:               %s\nTipo:               %s'%(conosco.nombre, conosco.colorhojas, conosco.colortallo, conosco.tammin, conosco.tammax, conosco.clima, conosco.zona, conosco.tipo))
                
        else:
                print ('\n')
                print ('La planta no esta registrada\n')
                nombre = input('¿Cual es el nombre de la planta?: ')
                colorhojas = input('¿Cual es el color de las hojas (o flor) de la planta?: ') 
                colortallo = input('¿Cual es el color del tallo de la planta?: ')
                tammin = input('¿Cual es el tamaño minimo de la planta (en cm)?: ')
                tammax = input('¿Cual es el tamaño maximo de la planta (en cm)?: ')
                clima = input('¿Cual es el clima de la planta?: ')
                zona = input('¿Cual es la zona de la planta?: ')
                tipo = input('¿Cual es tipo de planta?: ')
                
                newplant.append(NewPlant(nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo))
                Plants.append(Plant(nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo))
                Recordar(nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo)
                Recordar2(nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo)
                
                print ("¡Planta registrada!")

if __name__ == '__main__':
    
        if (len(sys.argv) >= 2 and sys.argv[1] == '--ingeniero'):
                ingeniero()
        else:
                main()