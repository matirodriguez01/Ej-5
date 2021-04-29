import csv

from Alumno import Alumno

def cero():
    print('Hasta luego')
    input('Presione cualquier tecla para continuar...')


def uno():
    print('\n-OPCIÓN 1-\n')
    anio = int(input('Ingrese el año:\n'))
    div = str(input('Ingrese la división:\n'))
    print("Alumnos        Porcentaje\n")
    for i in range(len(listaalumnos)):
        if listaalumnos[i].getdiv() == div and listaalumnos[i].getanio() == anio:
            if listaalumnos[i].getfaltas() > Alumno.faltperm:
                print(f"{listaalumnos[i].getnombre()}     ,   {listaalumnos[i].getporcentaje()}%")

    input('\nPresione cualquier tecla para continuar...')


def dos():
    print('\n-OPCIÓN 2-\n')
    mod = int(input("Ingrese el nuevo numero de inasistencias permitidas:"))
    Alumno.cambiarpermitidas(mod)
    input('\nPresione cualquier tecla para continuar...')


switcher = {
    0: cero,
    1: uno,
    2: dos
}


def switch(opc):
    func = switcher.get(opc, lambda: print('\nOpción incorrecta'))
    func()


if __name__ == '__main__':

    listaalumnos = []

    archivo = open('Alumnos.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        listaalumnos.append(Alumno(fila[0], fila[1], fila[2], fila[3]))
    archivo.close()

    band = False
    while not band:
        print('-----MENU-----')
        print('1- Mostrar alumnos con mas inasistencias de las permitidas')
        print('2- Modificar la de inasistencias')
        print('0- Salir')
        op = int(input('\nIngrese una opción: '))
        switch(op)
        band = int(op) == 0