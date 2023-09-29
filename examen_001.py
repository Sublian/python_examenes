"""
Prueba tecnica en coderbyte
Genere un codigo que reciba una cadena de texto como entrada, de la cual se necesita que elimines los simbolos y espacios, donde a cada oracion le cambies la primera letra a mayucula con excepcion de la primera palabra
Por ultimo cuando tengas una funcion con el resultado tendras que utilizar un token, el cual necesitas para hacer una intercalacion de elementos
"""

strParam="Hello+world, nice*to meet you!"
token="12PY345"

#funcion base que prepara la string en base a la solicitud del problema
def conversion(strParam):
  cadena=""
  #elimino los simbolos, si es un alfabeto lo guardo sino creo un espacio en blanco
  for char in strParam:
      if char.isalpha():
          cadena+=char
      else:
          cadena+=" "
  
  #transformo a minusculas
  cadena=cadena.lower()
  
  #segmento las frase en palabras 
  palabras = cadena.split()
  
  #convierto en mayuscula solo la primera
  palabras=[palabras[0]] + [palabra.capitalize() for palabra in palabras[1:]]
  
  #con un ciclo for se puede hacer tambien la misma accion
  #for i in range(1, len(palabras)):
  #    palabras[i] = palabras[i].capitalize()
  
  #utilizo un join para unir las palabras agrupar en una sola frase
  return "".join(palabras)

#creo la funcion intercalar cadenas
def intercalar_cadenas(cadena1, cadena2):
    cadena1= conversion(cadena1)
    resultado = ""
    # Obtener la longitud de la cadena más larga
    longitud_maxima = max(len(cadena1), len(cadena2))
    
    # Iterar sobre la longitud máxima
    for i in range(longitud_maxima):
        # Obtener el carácter de la cadena1 si el índice está dentro de los límites
        if i < len(cadena1):
            resultado += cadena1[i]
        
        # Obtener el carácter de la cadena2 si el índice está dentro de los límites
        if i < len(cadena2):
            resultado += cadena2[i]
    
    return resultado

print("<Resultado> \n"+intercalar_cadenas(strParam, token))
