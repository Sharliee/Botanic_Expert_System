"""

Nombre:      Carlos Andres Riveramelo Del Toro
Materia:     Sistemas Expertos
Docente:     Mauricio Alejandro Cabrera Arellano

"Sistema Experto En Plantas (El Mamalon Del Ingeniero Gutierrez)"

"""


"Modulo del ingeniero"

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
        
        nombre=input('Introduce el Nombre de la planta: ')
        colorhojas=input('Introduce el color de las hojas de %s: ' %(nombre))
        colortallo=input('Introduce el color de el tallo de %s: '%(nombre))
        tammin=input('Introduce el tamaño minimo de %s: '%(nombre))
        tammax=input('Introduce el tamaño maximo de %s: '%(nombre))
        zona=input('Introduce la zona donde crece %s: '%(nombre))
        
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
        
"Modulo del conocimiento"

class Planta(object):
        def __init__(self, nombre, colorhojas, colortallo, tammin, tammax, clima, zona, tipo):
                super(Planta, self).__init__()
                self.nombre = nombre
                self.colorhojas = colorhojas
                self.colortallo = colortallo
                self.tammin = tammin
                self.tammax = tammax
                self.clima = clima
                self.zona = zona
                self.tipo = tipo
        def mostrarPlanta(self):
                print ("%s %s %s %s %s %s %s" %(self.nombre, self.colorhojas, self.colortallo, self.tammin, self.tammax, self.zona, self.tipo))
Plantas=[]

class Perfil(object):
        def __init__(self, nombre1, zona1, tipo1):
                super(Perfil, self).__init__()
                self.nombre1 = nombre1
                self.zona1 = zona1
                self.tipo1 = tipo1
perfiles=[]
        
def cargaConocimientoPlantas():
        n = 0
        file = open('conocimiento','r')
        while True:
                pass
                n = n+1
                linea = file.readline()
                if not linea: break
                plnt = linea.split('|')
                Plantas.append(Planta(plnt[0], plnt[1], plnt[2], plnt[3], plnt[4], plnt[5], plnt[6], plnt[7]))
cargaConocimientoPlantas()

def cargaConocimientoPerfiles():
        file=open ('Perfiles','r')
        while True:
                pass
                linea = file.readline()
                if not linea: break
                per = linea.split('|')
                perfiles.append(Perfil(per[0], per[1], per[2], per[3], per[4]))
cargaConocimientoPerfiles()

def OAV():
        OAV = open('OAV','w')
        file = open('conocimiento','r')
        while True:
                pass
                linea = file.readline()
                if not linea: break
                plnt = linea.split('|')
                OAV.write('Objeto           Atributo         Valor')
                OAV.write('\n')
                OAV.write('\nPlanta     Nombre               '+plnt[0])
                OAV.write('\nPlanta     Color de Hojas       '+plnt[1])
                OAV.write('\nPlanta     Color de Tallo       '+plnt[2])
                OAV.write('\nPlanta     Tamaño Minimo        '+plnt[3])
                OAV.write('\nPlanta     Tamaño Maximo        '+plnt[4])
                OAV.write('\nPlanta     Clima                '+plnt[5])
                OAV.write('\nPlanta     Zona                 '+plnt[6])
                OAV.write('\nPlanta     Tipo                 '+plnt[7])
                OAV.write('\n\n\n')
        OAV.close()
        file.close()
OAV()
def Recordar(nombre, zona1, tipo1):
        file= open('Perfiles','a')
        file.write('\n')
        file.write(str(nombre)+'|'+str(zona1)+'|'+str(tipo1))
        file.close()

"Modulo de inferencia"

def Desconocido(nombre):
        for x in range(len(perfiles)):
                pass
                if (nombre == perfiles[x].nombre):
                        return perfiles[x]
                elif (x==len(perfiles) and nombre != perfiles[x].nombre):
                        return False
                    
def planta(dias, numerodia, semana, tipoalimento):
        
        Arboles_1=[]
        Plantas_Suculentas=[]
        Plantas_Trepadoras=[]
        Epifitas_Hemiepifitas=[]
        Parasitas_1=[]
        Saprofitas_1=[]
        Higuerones_1=[]
        Helechos_1=[]
        Hepaticas_1=[]
        Plantas_Insectivoras=[]
        for x in range(len(Plantas)):
                pass
                if ('Arboles' in Plantas[x].tipo):
                        pass
                        Arboles_1.append(Plantas[x])
                if ('Plantas Suculentas' in Plantas[x].tipo):
                        pass
                        Plantas_Suculentas.append(Plantas[x])
                if ('Plantas Trepadoras' in Plantas[x].tipo):
                        pass
                        Plantas_Trepadoras.append(Plantas[x])
                if ('Epifitas y Hemiepifitas' in Plantas[x].tipo):
                        pass
                        Epifitas_Hemiepifitas.append(Plantas[x])
                
                if ('Parasitas' in Plantas[x].tipo):
                        pass
                        Parasitas_1.append(Plantas[x])
                if ('Saprofitas' in Plantas[x].tipo):
                        pass
                        Saprofitas_1.append(Plantas[x])
                if ('Higuerones' in Plantas[x].tipo):
                        pass
                        Higuerones_1.append(Plantas[x])
                if ('Helechos' in Plantas[x].tipo):
                        pass
                        Helechos_1.append(Plantas[x])
                if ('Hepaticas' in Plantas[x].tipo):
                        pass
                        Hepaticas_1.append(Plantas[x])
                if ('Plantas Insectivoras' in Plantas[x].tipo):
                        pass
                        Plantas_Insectivoras.append(Plantas[x])
                