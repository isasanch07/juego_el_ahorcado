from random import *

#Crear una lista de palabras, la palabra se elije al azar con choice
#Funciones para pedir letra, validar letra, verificar si gana o pierde 

def palabras():
    lista = ["manguito", "cuna", "erizo", "aviones", "salpicon"]
    palabra = choice(lista)
    return palabra

#rallitas para adivinar la palabra
def lineas(palabra):
    largo = len(palabra)
    print("\n")
    linea = list("_"*largo)
    return(linea)

#print(lineas("Cocacola"))

def adivinar_palabra(palabra):
    lista_palabra = lineas(palabra) #Hacemos uso de la función de líneas
    oportunidades = len(palabra) #Tendra tantas oportunidades, como letras la palabra
    intentos = 0
    while (intentos < oportunidades):
        letra = input("Ingresa una letra: ")
        palabra = list(palabra) #La palabra se inserta en una lista  
        if letra in lista_palabra:
            print("Ya adivinaste esa letra") 
            continue
        elif letra in palabra:
            indice = palabra.index(letra)
            lista_palabra[indice] = (letra)
            print(lista_palabra)
            if lista_palabra == palabra:
                return"Has ganado!"
            else: 
                continue
        else: 
            intentos += 1
            restante = oportunidades - intentos
            if restante == 0:
                print(f"Perdiste! La palabra era: {palabra}") 
            else: 
                print(f"Letra incorrecta, te quedan {restante} intentos")
           
        
palabra = palabras() #Una palabra al azar se almacena en la variable "palabra"
print(lineas(palabra)) #Se muestra en pantalla las líneas acordes a la palabra seleccionada 
print(adivinar_palabra(palabra)) #Intentamos adivinar las letras que van
