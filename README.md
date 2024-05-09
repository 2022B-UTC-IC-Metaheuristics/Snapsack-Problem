# Knapsack-Problem

## 1 - Introducción ##
El problema de la mochila es uno de los 21 problemas NP-completos establecidos por el informático teórico Richard Karp en un famoso artículo de 1972. El problema de la mochila, comúnmente abreviado por KP, es un problema de optimización combinatoria, es decir, que busca la mejor solución entre un conjunto finito de posibles soluciones a un problema.

## 2 - Problema ##
Dado un conjunto de artículos, cada uno con un peso y un valor, el objetivo es determinar qué artículos incluir en una colección de manera que:

- El peso total no exceda un límite dado.
- El valor total sea lo más grande posible.

En este problema, se deben empaquetar un conjunto de artículos, con valores y tamaños dados (como pesos o volúmenes), en un contenedor con una capacidad máxima. Si el tamaño total de los artículos excede la capacidad, no se pueden empaquetar todos. En ese caso, el problema es elegir un subconjunto de los artículos de máximo valor total que quepan en el contenedor.

Velasco se basa en la definición formal del problema: *"Se tiene una determinada instancia de KP con un conjunto de objetos* $N$, *que consiste de* $n$ *objetos* $j$ *con ganancia* $p_j$ *y peso* $w_j$, *y una capacidad* $c$. *(Usualmente, los valores toman números enteros positivos). El objetivo es seleccionar un subconjunto de* $N$ *tal que la ganancia total de esos objetos seleccionados es maximizada y el total de los pesos no excede a* $c$".

  ### 2.1 - Definición ###

El modelo del KP parte de la suposición de que un escalador tiene que llenar su mochila. Para ello debe seleccionar una cantidad de varios posibles objetos, los cuales le pueden brindar el mayor beneficio sin exceder la capacidad de la mochila. El KP pueder ser matemáticamente formulado con un vector de variables binarias $x_j$ en donde:

$$x_{j}= \left\lbrace\begin{matrix}
1&si&el&elemento&j&es&seleccionado\\ 
0&en&otro&caso
\end{matrix}\right.$$

Entonces, si $p_j$ es una medida de importancia (en este caso, ganancia) para un elemento $j$, $w_j$ representa el tamaño de dicho elemento, y $cv$ es el tamaño de la mochila, el problema refiere a la selección de la cantidad de todos elementos cuyos vector binarios $x_j$ satisfagan las siguientes restricciones:

$$ \sum_{j=1}^{n} w_{j} x_{j} \leq cv $$

$$ x_{j}\in \left\lbrace 0,1 \right\rbrace , j=1,...,n $$

que deben contribuir a maximizar la siguiente función objetivo:

$$\sum_{j=1}^{n} p_{j} x_{j}$$

Para este caso se extendió el modelo con una restricción adicional de tamaño: $cv$ se considera como la capacidad volumétrica de la mochila y $cz$ como la capacidad en peso de la mochila. De esta manera se tienen dos variables para cada elemento: $w_j$ como el tamaño en volumen (cm cúbicos) del elemento $j-esimo$, y $z_j$ como el tamaño en peso (kg) del elemento $j-esimo$, lo cual da la siguiente restricción:

$$\sum_{j=1}^{n} z_{j} x_{j} \leq cz$$

### 2.2 - Aplicaciones ###

Como parte de la aplicación del problema de la mochila se emulan situaciones reales donde es necesario acomodar artículos de diferentes dimensiones en un espacio reducido.

Se puede emplear, como ejemplo, el uso de contenedores en las aduanas, donde se requiere enviar ítems de diferentes pesos, tamaños y valores de beneficio. Por otra parte, en la misma aduana, es necesario almacenar temporalmente los contenedores mismos, por lo que este problema puede ser resuelto con base en las soluciones propuestas para el problema de la mochila.

En aspectos de criptografía, al descifrar contraseñas, este problema se puede ver como un número de contenedores que pueden tener $n$ valores cada uno. De manera similar, al traducir un texto encriptado, al identificar los espacios, cada palabra puede fungir como un contenedor de $n_i$ ítems (caracteres de la palabra), donde cada caracter $i$ puede tener $n$ posibles artículos.

Además de las aplicaciones mencionadas anteriormente, el problema de la mochila también se utiliza en el ámbito de la ayuda humanitaria. Por ejemplo, al considerar la carga de un avión que transporta suministros de ayuda a áreas afectadas por desastres naturales o crisis humanitarias, se enfrenta el desafío de maximizar el valor total de la ayuda sin exceder la capacidad de carga del avión. En esta situación, el problema se formula de manera similar al problema de la mochila, donde los artículos corresponden a los diferentes tipos de suministros de ayuda (por ejemplo, alimentos, medicinas, mantas) y sus respectivos valores y pesos se ajustan para maximizar la eficiencia de la entrega de ayuda.

Como parte de la aplicación del problema de la mochila, y haciendo una revisión de la literatura actual se pueden resolver problemas relacionados con:

* La selección de proyectos, donde cada proyecto se puede ver como un contenedor de diferentes ítems tales como: personas, recursos, etc.

* La solución de problemáticas donde es necesario detectar patrones de corte.

* Situaciones de problemas de distribución de carga (física, eléctrica, etc.).

* El abastecimiento de vehículos de transporte y entrega de productos de diferentes tamaños que deben ser colocados en múltiples compartimentos de igual o diferente tamaño,

* La asignación de procesadores y datos en sistemas distribuidos.

### 2.3 - Ejemplo ###
  
|Elemento|Valor|Peso|
|--|--|--|
| A | 200 |40 |
| B | 80 | 20 |
| C | 30 | 15 |
| D | 15 | 20 |
| E | 10 | 80 |

Si la capacidad de la mochila es $c=70$ , meteríamos los elementos $A$ y $B$ que son los que mayor valor suman, y además ocupan toda la capacidad de la mochila.

## 3 - Modelo ##
  
  ### 3.1 - Función Objetivo ###
  
  Consiste en maximizar el valor que se llevará en la mochila
  
  ```Python
  def getTotalValor(actual_solution: list, valores: list, capacidad: int, pesos: list) -> float:
      """
      Calcula el valor total de una solución dada y verifica si excede la capacidad dada.
  
      Parámetros:
      - actual_solution (list): Una lista que representa la solución actual.
      - valores (list): Una lista de valores asociados a los elementos.
      - capacidad (int): La capacidad máxima permitida.
      - pesos (list): Una lista de pesos asociados a los elementos.
  
      Retorna:
      - float: El valor total de la solución actual.
               Si el total del peso excede la capacidad, retorna la diferencia entre el valor total y el total del peso.
      """
      totalValor = 0
      i = 0
      for element in actual_solution:
          if element:
              totalValor += float(valores[i])
          i += 1
      totalPeso = 0
      i = 0
      for element in actual_solution:
          if element:
              totalPeso += pesos[i]
          i += 1
      totalPeso=int(totalPeso)
      if totalPeso > capacidad:
          return totalValor-totalPeso
      return totalValor
  ```
  ### Ejemplo de llamada
  ```Python
    costo = functools.partial(getTotalValor, valores=valores, capacidad=capacidad, pesos=pesos)
 ```
  ### 3.2 - Representación de la solución ###
  
  Definimos la capacidad de la mochila
  
  ```Python
  cap=30
  ```
  
  Se definieron dos vectores
  
  ```Python
  v=np.array([20,4,25,2,8])
  p=np.array([10,2,14,8,5])
  ```
  
  El vector $v$ contiene los valores de los elementos propuestos para la mochila, mientras que el vector $p$ contiene los pesos de cada uno de los elementos. Tenemos entonces $5$ objetos con $2$ características: valor y peso.
  
  Al ejecutar el programa, nos lanza como solución un vector como éste
  
  ```Python
  Solucion:  [1, 0, 1, 0, 1]
  Costo:  53.0
  ```
  en el cuál, se mostrarán con un 1 los objetos seleccionados para introducirse en la mochila, mientras que con 0 los que    se quedarán afuera.
  
  
## 4 - Instancias ##

La siguiente tabla muestra las instancias que se van a resolver.
  | Instancias | Tamaño de vector solución | Capacidad | costo | solucion |
|-----------|-----------|-----------|-----------|-----------|
| 1  | 20  | 50  |  131.0 |  [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1] |
| 2  | 100  | 500  | 792.0  | [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1] |
| 3  | 200  | 1000  | 1803.0  | [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0] |

  
Codigo para leer los archivos
```Python
pesos = []
with open("./instancias/p20.txt", "r") as file:
    for line in file:
        row = line.strip().split(",")
        pesos.append(row)
pesos = np.array(pesos).astype("float")

valores = []
with open("./instancias/v20.txt", "r") as file:
    for line in file:
        row = line.strip().split(",")
        valores.append(row)
valores = np.array(valores).astype("float")
```

## 5 - Referencias ##

Velasco, J. (2010). NP-Completeness: Complejidad del problema de la Mochila. Presentación de Tesis. Facultad de Ingeniería Mecánica y Eléctrica. División de Posgrado en Ingeniería en Sistemas. Universidad Autónoma de Nuevo León.

De Hidalgo, U. A. D. E. (s. f.). Boletín Científico :: UAEH. https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n6/e2.html 
