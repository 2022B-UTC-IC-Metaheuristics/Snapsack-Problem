# Snapsack-Problem

## 1 - Introducción ##

El problema de la mochila, comúnmente abreviado por KP es un problema de optimización combinatoria, es decir, que busca la mejor solución entre un conjunto finito de posibles soluciones a un problema.

## 2 - Problema ##
En éste problema, se deben empaquetar un conjunto de artículos, con valores y tamaños dados (como pesos o volúmenes), en un contenedor con una capacidad máxima. Si el tamaño total de los artículos excede la capacidad, no puede empacarlos todos. En ese caso, el problema es elegir un subconjunto de los artículos de máximo valor total que quepan en el contenedor.

  ### 2.1 - Definición ###

El modelo del KP parte de la suposición de que un escalador tiene que llenar su mochila. Para ello debe seleccionar una cantidad de varios posibles objetos, los cuales le pueden brindar el mayor beneficio sin exceder la capacidad de la mochila. El KP pueder ser matemáticamente formulado con un vector de variables binarias xj en donde:

![image](https://user-images.githubusercontent.com/56168184/160952740-33f0cf02-70b6-4fb5-9ef2-eee73867596d.png)

 Entonces, si pj es una medida de importancia (en este caso, ganancia) para un elemento j, wj representa el tamaño de dicho elemento, y cv es el tamaño de la mochila, el problema refiere a la selección de la cantidad de todos elementos cuyos vector binarios xj satisfagan las siguientes restricciones:
 
 ![image](https://user-images.githubusercontent.com/56168184/160952985-cf3104ea-0fe2-4ca3-bea4-43a685d29b9b.png)
 
 que deben contribuir a maximizar la siguiente función objetivo:
 
 ![image](https://user-images.githubusercontent.com/56168184/160953037-04cbb5fc-6cc1-4f45-94ac-eaab8e18292c.png)

Para este caso se extendió el modelo con una restricción adicional de tamaño: cv se considera la capacidad volumétrica de la mochila y cz se considera la capacidad en peso de la mochila. De esta manera se tienen dos variables de tamaño para cada elemento: wj el tamaño en volumen (cm cúbicos) de cada elemento, y zj el tamaño en peso (kg) del elemento, lo cual da la siguiente restricción:

![image](https://user-images.githubusercontent.com/56168184/160953207-106a1c06-8759-4e36-9eb8-7abfd032cb9f.png)

  ### 2.2 - Aplicaciones ###
  
Como parte de la aplicación del problema de la mochila como una forma de emular situaciones reales donde es necesario acomodar artículos de diferentes dimensiones en un espacio reducido.

Se puede emplear, como ejemplo, el uso de contenedores en las aduanas, donde se requiere enviar ítems de diferentes pesos, tamaños y valores de beneficio. Por otra parte, en la misma aduana, es necesario almacenar, de manera temporánea, los contenedores mismos, por lo que este problema puede ser resuelto con base en la soluciones propuesta para el problema de la mochila.

En aspectos de criptografía, en el caso de descifrar contraseñas, este problema se puede ver como un número de contenedores que pueden tener n valores cada uno. En otro sentido, cuando es necesario traducir un texto encriptado, en el momento de identificar los espacios, cada palabra puede fungir como un contenedor de ni ítems (caracteres de la palabra), donde cada caracter i puede tener n posibles artículos.

Como parte de la aplicación del problema de la mochila, y haciendo una revisión de la literatura actual se pueden resolver problemas relacionados con:

La selección de proyectos, donde cada proyecto se puede como un contenedor de diferentes ítems tales como: personas, recursos, etc.
En la solución de problemáticas donde es necesario detectar patrones de corte.
En situaciones donde se problemas de distribución de carga (física, eléctrica, etc.).
Cuando se requiere abastecer vehículos de transporte y entrega de productos de diferentes tamaños que deben ser colocados en múltiples compartimentos de igual o diferente tamaño,
Asignación de procesadores y datos en sistemas distribuidos.

  ### 2.3 - Ejemplo ###
  
|Elemento|Valor|Peso|
|--|--|--|
| A | 200 |40 |
| B | 80 | 20 |
| C | 30 | 15 |
| D | 15 | 20 |
| E | 10 | 80 |

Si la capacidad de la mochila es c=70, meteríamos los elementos A y B que son los que mayor valor suman, y además ocupan toda la capacidad de la mochila.

## 3 - Modelo ##
  
  ### 3.1 - Función Objetivo ###
  
  Consiste en maximizar la carga que se llevará en la mochila
  
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
  
  Se definieron dos vectores
  
  ```Python
  v=np.array([20,4,25,2,8])
  p=np.array([10,2,14,8,5])
  ```
  
  El vector v contiene los valores de los elementos propuestos para la mochila, mientras que el vector p contiene los pesos   de cada uno de los elementos. Tenemos entonces 5 objetos con 2 características: valor y peso.
  
  Al ejecutar el programa, nos lanza como solución un vector como éste
  
  ```Python
  ([1,0,0,0,0])
  ```
  en el cuál, se mostrarán con un 1 los objetos seleccionados para introducirse en la mochila, mientras que con 0 los que    se quedarán afuera.
  
  ### 3.4 - Solución vecino ###
  
  Para generar una solución vecino, el programa recorre el vector de soluciones, se genera también un número entre 0 y 1. 
  
  Si ese número es mayor a 0.5, quiere decir que ese objeto será parte de la solución.
  
## 4 - Instancias ##

### Primera instancia: ###
  
  capacidad = 40
  items = [0,0,0,0,0]
  valores = [20,4,25,2,8]
  pesos = [10,2,14,8,5])
  
Resultado = [0,1,1,1,1]

### Segunda instancia: ###
  
  capacidad = 50
  items = [0,0,0,0,0]
  valores = [30,10,20,15,8]
  pesos = [5,20,25,18,30])
  
Resultado = [1,1,1,0,0]
