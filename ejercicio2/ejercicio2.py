import json
cadena = "Érase una vez una niñita que lucía una hermosa capa de color rojo. Como la niña la usaba muy a menudo, todos la llamaban Caperucita Roja. Un día, la mamá de Caperucita Roja la llamó y le dijo: —Abuelita no se siente muy bien, he horneado unas galletitas y quiero que tú se las lleves. —Claro que sí —respondió Caperucita Roja, poniéndose su capa y llenando su canasta de galletas recién horneadas. Antes de salir, su mamá le dijo: — Escúchame muy bien, quédate en el camino y nunca hables con extraños . — Yo sé mamá — respondió Caperucita Roja y salió inmediatamente hacia la casa de la abuelita.”

# Se nos comento que puede tener comas y puntos pero de igual manera agregue salto de linea
discriminar = "—,..:-\n!\""

# Remplazamos por vacio los caracteres antes mencionados
for caracter in discriminar:
     cadena = cadena.replace(caracter,"")  
          
# Lo convertimos a minúsculas la cadena para facilitar el conteo ya que puede ser mayusculas 
# la misma palabra 
cadenamini = cadena.lower()

# Convertimos la cadena en un arreglo usando los espacios
palabras = cadenamini.split(" ")

#Usaremos un diccionario
diccionarioContador = {} 

# en un ciclo contaremos las palabras
for palabra in palabras: 
    if palabra in diccionarioContador:
        diccionarioContador[palabra] += 1
    else:
        diccionarioContador[palabra] = 1
        
 #Codificamos con json.dumps el cual no habia utilizado, al igual que ensure_ascii=False para los acentos
json = json.dumps(diccionarioContador, indent = 1,ensure_ascii=False)   
print(json)  