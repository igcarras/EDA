""" Ayuda a la detección de plágio en entregas de ejercircios en Python
Puesto a punto por Álvaro Somolinos. Departamento de CC de la Computación UAH01/04/20"""
#Pese a CAMBIO IDENTIF y COMENTARIOS
#Pese a CAMBIAR SANGRADO (frecuente si copian de papel)
#Pese a OLVIDAR COPIAR LINEAS
#REsiste peor el cambio de orden
import os
import pycode_similar
    #https://pypi.org/project/pycode-similar/
import Levenshtein
def ajusteParam (DIR):
    """str-->
    OBJ: Orienta en los parámeros de Levenshtein y pycode"""
    files = os.listdir(DIR)
    python_files = []
    sim=[]       #pycode_similaridades totales
    lev=[]       # distancias de Liev totales
    for file in files:
        if file.endswith('.py'):
            python_files.append(file)
    print(' '*26,'SIM', ' '*8, 'LEV')
    for i in range(len(python_files)):
        print(' '*20,python_files[i])
        for j in range(len(python_files)):
            if i!=j:
                with open(f'{DIR}/{python_files[i]}', 'r', encoding='utf8') as file_1:
                    content_1 = file_1.read()
                with open(f'{DIR}/{python_files[j]}', 'r', encoding='utf8') as file_2:
                    content_2 = file_2.read()
                distancia = Levenshtein.ratio(content_1, content_2)
                lev.append(distancia)
                try:
                    result = pycode_similar.detect([content_1, content_2], diff_method = pycode_similar.UnifiedDiff)
                    percent = result[0][1][0].plagiarism_percent
                except:
                    percent = -1
                else: sim.append(percent)
                print('%20s, %12f, %12f' %(python_files[j], percent,distancia))
    print( '%16s%12s%12s'%('MIN','AVG','MAX'))
    print('SIM=','%12f%12f%12f' %(min(sim), sum(sim)/len(sim), max(sim)))
    print('LEV=','%12f%12f%12f'%( min(lev), sum(lev)/len(lev), max(lev)))
#ajusteParam ('./calibrado')
#EN esta versión se contrastan todos con todos para que salga lista en orden alfabético
#si el nombre del fichero es el nombre del alumno. Duplica el trabajo
LEV=0.72            # max distancia caracteres
COD=0.99              # Max código python
print ('PARAMETRIZACION LEV=', LEV, 'COD=',COD)
DIR = '.'  #directorio a analizar
files = os.listdir(DIR)
python_files = []
for file in files:
    if file.endswith('.py'):
        python_files.append(file)
contAl=0                                 #alumnos copian
totNoCompila=0
numArch=len(python_files)
for i in range(numArch):
    print(f'--- Comparando {python_files[i]} ---')
    contE=0
    compila=0
    for j in range(numArch):
        if i!=j:
            with open(f'{DIR}/{python_files[i]}', 'r', encoding='utf8') as file_1:
                content_1 = file_1.read()
            with open(f'{DIR}/{python_files[j]}', 'r', encoding='utf8') as file_2:
                content_2 = file_2.read()
            try:
                result = pycode_similar.detect([content_1, content_2], diff_method = pycode_similar.UnifiedDiff)
                percent = result[0][1][0].plagiarism_percent
            except Exception:
                percent = -1        #si no compila uno de los comparados, solo veo distancia de Levenshtein
                compila+=1
            distance_percent = Levenshtein.ratio(content_1, content_2)
            #print(percent,distance_percent)
            #if percent >= COD and distance_percent >= LEV :
            if percent >= COD or distance_percent >= LEV :
                print ('Posible plagio con %20s%12f,   %12f' %(python_files[j],percent, distance_percent))
                contE+=1
    if contE>0: contAl+=1
    print('similar a', contE, 'Compila=', compila==numArch-1)
    if compila==numArch-1: totNoCompila+=1
print('detectadas', contAl, 'copias de=', numArch, ', no campilan=', totNoCompila)
''' #si no se requiere el lustado ordenado
LEV=0.65                # max distancia caracteres
COD=0.85                # Max código python
DIR = './Prueba de copias VALIDACION1'    #directorio a analizar
files = os.listdir(DIR)
python_files = []
for file in files:
    if file.endswith('.py'):
        python_files.append(file)
contAl=0
for i in range(len(python_files)):
    print(f'--- Comparando {python_files[i]} ---')
    contE=0
    for j in range(i+1,len(python_files)):
        with open(f'{DIR}/{python_files[i]}', 'r', encoding='utf8') as file_1:
            content_1 = file_1.read()
        with open(f'{DIR}/{python_files[j]}', 'r', encoding='utf8') as file_2:
            content_2 = file_2.read()
        try:
            result = pycode_similar.detect([content_1, content_2], diff_method = pycode_similar.UnifiedDiff)
            percent = result[0][1][0].plagiarism_percent
        except Exception:
            percent = -1
        distance_percent = Levenshtein.ratio(content_1, content_2)
        if percent > COD and distance_percent > LEV:
            print(f'Posible plagio con {python_files[j]}: {percent}, {distance_percent}')
            contE+=1
        if contE>0: contAl+=1
    print('similar a ', contE)
print('detectados', contAl, 'Alumnos en copias')
'''
