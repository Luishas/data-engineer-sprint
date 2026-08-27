## CTE (Common Table Expression):
- Sirve para anidar todos los queries a usar temporalmente y no tener una mala distribucionn de los mismos

## Window Functions:
- Nos permite colapsar filas para realizar consultas pero sin dejar de lado los demas, en lugar de usar GROUP BY que solo trae lo que  se indica, se usa PARTITION BY para usar todas las caracteristicas dentro del query

## UPSERT:
- Permite realizar consultas sin remover los datos que ya fueron subidos, si no verificar si se encuentran creados, y crear uno nuevo, pero no reemplazar los datos ya creados para no perder ninguno

## INDEX
- Sirve para poder encontrar datos mas facilmente, usando su indice como motor de busqueda principal

## VIEWS
- son querys los cuales puedes guardar con un nombre especifico, para luego invocarlos usando ese nombre y correr el query

## TRANSACTIONS
- Son agrupaciones de querys en las cuales si una falla, no se ejecuta ninguna, y si todo corre sin problemas se ejecutan todas al mismo tiempo, ademas de poder ofrecernos rollbacks en caso alguna falle y no tengamos data partida.