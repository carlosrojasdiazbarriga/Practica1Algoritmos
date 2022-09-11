import os


def burbuja_simple(arr,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)   
    
def insertSort(arr,n):
    
    for i in range(1,n):
        insert_value = arr[i]
        insert_index = i 
        
        while insert_index > 0 and arr[insert_index - 1] > insert_value:
            arr [insert_index] = arr [insert_index - 1]
            insert_index -=1
            
        arr[insert_index] = insert_value
        
    
    print(arr)    
    return arr

def shellSort(arr,n):
    interval = n // 2
    
    while interval > 0:
        for i in range(interval,n):
            insert_value = arr[i]
            insert_index = i 
            
            while insert_index > 0 and arr[insert_index-interval] > insert_value:
                arr[insert_index] = arr[insert_index - 1]
                insert_index -= 1
                
            arr[insert_index] = insert_value  
        interval //= 2
        
    print(arr)
    return arr
            


def lectura(num_lines):
    line_int=[]
    index=2
    with open('na.txt', 'r') as f:
        for line in f:
            line_int.extend(int(i) for i in line.split())
            if index <= num_lines:
                index += 1
            else:
                break
    return line_int
     


def inicio():
    print('ingresa le numero de enteros a ordenar')
    n= int(input())
    arr=lectura(n)
    
def opcionMain(select):
    # switch diccionario
    return {
        0: quit,
        1: burbuja_simple,
        3: insertSort,
        5: shellSort,
    }.get(select, 'error')


def menuPrincipal():
    print('----------------------------------------------------------------')
    print('Practica 1 Selecciona un metodo de ordenamiento')
    print('0. salir')
    print('1. Burbuja Simple')
    print('2. Burbuja Mejorada')
    print('3. insercion')
    print('4. Seleccion')
    print('5. Shell')
    
    seleccion = int(input())
    
    print('ingresa le numero de enteros a ordenar')
    n= int(input())
    arr=lectura(n)
    
    funcion = opcionMain(seleccion)
    if funcion == 'error':
        print('Esa no es una opcion valida')
        print('volviendo menu principal')
        return
    else:
        resultado = funcion(arr,n)
        return resultado


try:
    menuPrincipal()
except KeyboardInterrupt:
    quit()
except: 
    print('///////ocurrio un error de entrada regresando al menu////////')