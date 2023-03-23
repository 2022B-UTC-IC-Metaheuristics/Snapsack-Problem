# Snapsack-Problem

## 1 - Introducción ##

El problema de la mochila, comúnmente abreviado por KP es un problema de optimización combinatoria, es decir, que busca la mejor solución entre un conjunto finito de posibles soluciones a un problema.

## 2 - Problema ##
En éste problema, se deben empaquetar un conjunto de artículos, con valores y tamaños dados (como pesos o volúmenes), en un contenedor con una capacidad máxima. Si el tamaño total de los artículos excede la capacidad, no se pueden empaquetar todos. En ese caso, el problema es elegir un subconjunto de los artículos de máximo valor total que quepan en el contenedor.

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
  
Como parte de la aplicación del problema de la mochila como una forma de emular situaciones reales donde es necesario acomodar artículos de diferentes dimensiones en un espacio reducido.

Se puede emplear, como ejemplo, el uso de contenedores en las aduanas, donde se requiere enviar ítems de diferentes pesos, tamaños y valores de beneficio. Por otra parte, en la misma aduana, es necesario almacenar, de manera temporal, los contenedores mismos, por lo que este problema puede ser resuelto con base en la soluciones propuesta para el problema de la mochila.

En aspectos de criptografía, en el caso de descifrar contraseñas, este problema se puede ver como un número de contenedores que pueden tener $n$ valores cada uno. En otro sentido, cuando es necesario traducir un texto encriptado, en el momento de identificar los espacios, cada palabra puede fungir como un contenedor de $n_i$ ítems (caracteres de la palabra), donde cada caracter $i$ puede tener $n$ posibles artículos.

Como parte de la aplicación del problema de la mochila, y haciendo una revisión de la literatura actual se pueden resolver problemas relacionados con:

La selección de proyectos, donde cada proyecto se puede ver como un contenedor de diferentes ítems tales como: personas, recursos, etc.

* En la solución de problemáticas donde es necesario detectar patrones de corte.

* En situaciones donde de problemas de distribución de carga (física, eléctrica, etc.).

* Cuando se requiere abastecer vehículos de transporte y entrega de productos de diferentes tamaños que deben ser colocados en múltiples compartimentos de igual o diferente tamaño,

* Asignación de procesadores y datos en sistemas distribuidos.

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
  def Costo(sol,size):
    f=0
    for i in range(size):
        if sol[i] == 1:
            f+=v[i]
    return f
  ```
  
  ### 3.2 - Restricciones ###
  
  El peso de la carga transportada no puede exceder la capacidad máxima de la mochila
  
  ```Python
  if c > cap:
        sol = Genera_Vecino(size,cap)
  ```
  
  ### 3.3 - Representación de la solución ###
  
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
  ([1,0,1,0,1])
  ```
  en el cuál, se mostrarán con un 1 los objetos seleccionados para introducirse en la mochila, mientras que con 0 los que    se quedarán afuera.
  
  ### 3.4 - Solución vecino ###
  
  Para generar una solución vecino, el programa recorre el vector de soluciones, se genera también un número entre 0 y 1. 
  
  Si ese número es mayor a 0.5, quiere decir que ese objeto será parte de la solución.
  
  ```Python
  def Genera_Vecino(sol, size, cap):
    r = rn.randint(0, size-1)
    
    if sol[r] == 0:
        sol[r] = 1
    else:
        sol[r] = 0
    pSol = pesos(sol,size)
    while pSol > cap:
        i = rn.randint(0,size-1)
        sol[i] = 0
        pSol = pesos(sol,size)
        
    return sol
    
    def pesos(sol,size):
    f=0
    for i in range(size):
        if sol[i] == 1:
            f+=p[i]
    return f
  ```
  
## 4 - Instancias ##

El equipo determinó que para el vector de pesos, los valores se encuentren entre 1 y 20, por conveniencia.

### Primera instancia: ###
  
  Tamaño de vector solución = 20 items
  
  capacidad = 50

### Segunda instancia: ###

  Tamaño de vector solución = 200 items
  
  capacidad = 50

  ### Tercera instancia: ###

  Tamaño de vector solución = 1500 items
  
  capacidad = 50
  
Codigo para leer los archivos

![image](https://user-images.githubusercontent.com/56168184/165009779-6f8d27cc-1f40-423c-98a8-2d42fc69ee14.png)

