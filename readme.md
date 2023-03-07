# Requerimientos
**Objetivo**: Analizar un proceso realizado por una persona física, entender los pasos que se realizan en dicho proceso, y redactar el proceso o algoritmo que refleja los pasos necesarios para realizar dicha actividad.

**Situación a analizar**: Se desea escribir una carta utilizando letras recortadas de un artículo de una revista. Donde el primer paso es verificar que en dicho artículo existan todas las letras necesarias para lograr redactar la carta.

**Entregable del entrevistado**:  Plantee la resolución que considere más acorde para modelar el proceso antes mencionado. Lo que se evalúa es la lógica de la resolución propuesta y no el método usado, por lo tanto se puede hacer en texto estructurado, pseudocódigo, modelar la situación como un script usando un archivo donde está la carta a escribir y otro archivo donde está el artículo del cual se tomarán las letras o cualquier otra manera que considere apropiada.

# Solucion
El modelo planteado en `main.py` representa el algoritmo que una persona podria aplicar en la vida real para resolver la situacion. El proceso consta de 3 etapas: `verificar`, `recortar`, `armar`.

### Verificar
En esta etapa se tiene como entrada 2 elementos, la `carta` y el `articulo`, y tiene por objetivo determinar si la carta se puede `armar` con el contenido del `articulo`. 
 - Primero se obtienen las frecuencias de las letras necesarias en la carta y las letras disponibles en el `articulo` (se utilizo la clase `Counter` para simplificar la tarea, de haber creado un `dict` manualmente el proceso podria ir verificando a medida que calculando las frecuencias y asi cortar antes)
 - Luego se verifica por cada letra necesaria que la frecuencia sea `<=` a la disponible (o que la disponible sea `>` a la necesaria)
Al final de la etapa tendremos los siguientes elementos: la `carta`, el `articulo`, sus `frecuencias` de letras respectivas

### Recortar
Esta etapa tiene como entrada 3 elementos, el `articulo` y las frecuencias resultantes de la etapa anterior, tiene por objetivo `recortar` o remover del articulo las letras necesarias para `armar` la carta. 
-  Se recorre de forma secuencial el articulo y por cada se verifica si es necesario recortarla o no
   - Si verifica que en la lista de frecuencia de la `carta` existe la letra entonces recorta la letra

Al final se devuelven 2 elementos: el valor del `articulo` sin las letras recortadas y las letras recortadas (en el script seria equivalente a utilizar la lista de frecuencias de la `carta`, pero a modo de representar la realidad se almacena en otro `Counter`)

### Armar
La etapa final de armado tiene por entrada la `carta` y las `letras recortadas`, y tiene por objetivo construir un nuevo texto con las `letras recortadas` cuyo contenido sea igual al contenido de la `carta`.
Para este caso se utilizo la misma estrategia que para el recortecon la diferencia de que en vez de recortar,se pega una letra nueva

# Notas

- Notese que para obtener el mismo resultado el script podria reducirse a la primera etapa de verificacion y retornar el contenido de la carta (si no se tuviera en cuenta el proceso).
- Otro approach posible podria ser considerar palabras o grupos de letras, esto reduciria la cantidad de pasos en general.
- El script deberia funcionar para python3.6 en adelante
