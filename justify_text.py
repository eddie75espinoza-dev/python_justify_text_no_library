# -*- coding: utf-8 -*-
"""
Dev: Eddie Espinoza
date: 26/11/2021

Hacer un programa en python que "justifique" un texto con fuente monoespaciada.


⚠️ no usar ninguna librería, solo Python puro



### Input

- Un string de una sola linea
- El ancho de la línea esperada

Ninguna palabra del string será más larga que el ancho de línea esperado.

### Output

Mostrar por standard output el texto justificado, de acuerdo a las siguientes reglas:

- Use espacios para separar las palabras
- Cada línea deberá contener la mayor cantidad de palabras posibles
- Usar \n para separar líneas
- El máximo y el mínimo gap de una misma fila no puede diferir en más de 1 espacio
    - Incorrecto: Lorem-----ipsum--dolor
    - Correcto: Lorem----ipsum---dolor
- Las líneas deberán terminar en una palabra, no un espacio
- '\n' no está incluido en el largo de una línea
- Espacios más largos van primero, luego los espacios más pequeños.
    - Correcto: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 espacios).
    - Incorrecto: 'Lorem--ipsum--dolor---sit---amet' (2, 2, 3, 3 espacios).
- La última línea no estará justificada, sólo un espacio entre palabras
- Líneas con una sola palabra larga no necesitan espacios ('unapalabralarga\n').

## Ejemplo:

### Input:

```
La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera.
```

Largo de la línea: 30

### Output:

```
La  historia de la ópera tiene
una   duración   relativamente
corta  dentro  del contexto de
la  historia  de  la música en
general:  apareció   en  1597,
fecha   en   que  se  creó  la
primera ópera.
```

☝ Notar que todas las líneas, salvo la última, terminan exactamente en la misma columna. Esa es la idea de justificar.

"""
def justify_text(text, max_width:int):
    lst_words = []
    result = []
    n = 0
    for w in text:
        while len(w) + n + len(lst_words) > max_width:
            gaps = (len(lst_words) - 1) or 1
            q, rem = divmod(max_width - n, gaps)
            for i in range(gaps):
                lst_words[i] += " " * q + (" " if i < rem else "")
            result.append("".join(lst_words))
            n,  lst_words = 0, []
        lst_words.append(w)
        n += len(w)

    line = result + [" ".join(lst_words).ljust(max_width)] if lst_words else []

    return line

    

if __name__ == '__main__':
    
    #mySentence = input('Escriba una Oración: ').strip()
    myText = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera.".split()
    lineWidth = int(input("Largo de la línea: "))

    #print("Texto original:\n",myText)

    lst_result = justify_text (myText, lineWidth) # devuelve una lista con el resultado
    
    for txt in lst_result:
        print(txt)