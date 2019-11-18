# Complejidad Algorítmica
## Trabajo Final
### Seción CC41 - Tema: Problema de corte y empaquetamiento 3D
### Integrantes:

* Claudia Miranda
* Rodrigo Cuenca

### INTRODUCCIÓN

Nuestro proyecto se basa en encontrar la solución a un problema sobre optimización de espacios para objetos tridimensionales. Para este proyecto estaremos implementando los algoritmos de: Fuerza Bruta, Backtracking. Lo que se espera de este proyecto es comparar los algoritmos implementados y analizar la eficencia de cada uno de ellos en la problemática presentada.

### PROBLEMA

En este proyecto se capto como problema principal el desperdicio de recursos. Este puede ser minimizado con un empaquetamiento adecuado; y, en este caso tambien hay un abuso excesivo de cortes. 
Para ambos problemas mencionados, existen algoritmos que representan soluciones exactas y otros que representan
soluciones que hacen uso de heurísticas. Finalmente, una empresa debe decidir que problema prefiere atacar, o si desea
atacar ambos, y que tipo de solución es mas conveniente usar; para lo cual, debe analizar y discutir las ventajas y
desventajas que conlleva cada algoritmo.


### OBJETIVOS

**Objetivo General:** 
- Al finalizar el curso,el estudiante genera distintos algoritmos de corte y empaquetamiento basándose en técnicas tales como Fuerza Bruta y BackTracking teniendo en cuenta las restricciones impuestas en clases.

**Objetivos Específicos:**
1. **Crear** algoritmos que solucione el problema de cortes y empaquetamientode con distintos métodos por integrante.
2. **Implementar una interfaz** que le permita al usuario ingresar los datos necesarios y que el programa sea capaz de mostrar  los distintos resultados o implementar la posibilidad de ueasr archivos para la carga y escritura de estos.
3. **Hallar** la complejidad de los algoritmos propuestos.
4. **Generar** archivos de entrada, siguiendo el formato establecido
5. **Analizar** la eficiencia de las soluciones mediante:
- Porcentaje de desperdicio para el empaquetamiento y número de cortes (para los recortes)
- Tablas de comparación: tiempo de ejecución de algoritmo vs entrada de datos, memoria consumida por algoritmo vs entrada de datos 
6. **Presentar**  conclusiones finales en función de los datos levantados en el punto anterior.

### MARCO TEÓRICO

#### FUERZA BRUTA

En informática, la búsqueda por fuerza bruta es una técnica trivial pero muy usada, que consiste en probar sistemáticamente todas las posibles soluciones de un problema, hasta encontrarla. La búsqueda por fuerza bruta es usualmente sencilla de implementar y, siempre que exista, encuentra una solución. Sin embargo, su coste de ejecución es proporcional al número de soluciones candidatas, el cual es exponencialmente proporcional al tamaño del problema. 
Por otro lado, la búsqueda por fuerza bruta se utiliza cuando el número de soluciones candidatos es mínimo o cuando previamente se puede resolver por algún otro método heurístico.

#### PROGRAMACION DINAMICA

La programación dinámica es una técnica matemática que se utiliza para la solución de problemas matemáticos seleccionados, en los cuales se toma un serie de decisiones en forma secuencial. Frecuentemente para resolver un problema complejo se tiende a dividir este en subproblemas, más pequeños, resolver estos últimos (recurriendo posiblemente a nuevas subdivisiones) y combinar las soluciones obtenidas para calcular la solución del problema inicial.
La programación dinámica se emplea a menudo para resolver problemas de optimización que satisfacen el principio de optimalidad: en una secuencia óptima de decisiones toda subsecuencia ha de ser también óptima.

### CONCLUSIONES

**Fuerza Bruta**
Podemos utilizar fuerza bruta cuando queremos añadir las piezas de forma brusca para cumplir su objetivo. En este caso se realizó
un algoritmo que encuentre el primer espacio disponible para poder insertar las piezas de acuerdo a su área. Es sugerible que se use este algoritmo por su fácil implementación, pero no es recomendable cuando existen muchos datos de entrada, ya que su tiempo de ejecución es exponencial. 

**Programación dinámica**
Podemos utilizar programación dinámica en problemas de optimización que se pueda dividir en etapas y que sea dinámico en el tiempo puede resolverse por programación dinámica.
