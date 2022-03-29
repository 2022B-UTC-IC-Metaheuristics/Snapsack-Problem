# Snapsack-Problem

1 - Introducción
El problema de la mochila, comúnmente abreviado por KP es un problema de optimización combinatoria, es decir, que busca la mejor solución entre un conjunto finito de posibles soluciones a un problema.

2 - Problema
En éste problema, se deben empaquetar un conjunto de artículos, con valores y tamaños dados (como pesos o volúmenes), en un contenedor con una capacidad máxima. Si el tamaño total de los artículos excede la capacidad, no puede empacarlos todos. En ese caso, el problema es elegir un subconjunto de los artículos de máximo valor total que quepan en el contenedor.

  2.1 - Definición
El problema más común que se está resolviendo es el problema de la mochila 0-1, que restringe el número x de copias de cada tipo de artículo a cero o uno. Dado un conjunto de n artículos numerados del 1 al n, cada uno con un peso wi y un valor wi, junto con una capacidad máxima de peso W.

El problema de la mochila acotada (BKP) elimina la restricción de que solo hay uno de cada elemento, pero restringe el número x de copias de cada tipo de elemento a un valor entero máximo no negativo c.

  2.2 - Aplicaciones
Una de las aplicaciones que tiene éste problema en la vida real es la organización de los barcos cargueros para envíos internacionales. En éstos la prioridad es cargar los barcos con el mayor valor monetario posible.

  2.3 - Ejemplo
  
![image](https://user-images.githubusercontent.com/56168184/160521386-64e7d9d7-3220-4e4b-b8f2-40e3eb9bf370.png)

3 - Modelo
  
  ![image](https://user-images.githubusercontent.com/56168184/160303688-b27e0861-8814-4841-b121-ba4151bcf943.png)
  
  3.1 - Función Objetivo
  
  ![image](https://user-images.githubusercontent.com/56168184/160303674-29e4a221-06db-44bf-82a9-ab99ac0cd19d.png)
  
  3.2 - Restricciones
  
  ![image](https://user-images.githubusercontent.com/56168184/160303683-b557a005-1541-427b-a700-ab5e8e1452bd.png)
  
  3.3 - Representación de la solución
  
  3.4 - Solución vecino
  
4 - Instancias
