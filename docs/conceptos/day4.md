## FACT
- Es la tabla central en la cuál nosotros trabajaremos las consultas y los datos a manejar

## Dimension
- Son las tablas que poblan la tabla de factos, y tienen que responder a preguntas sobre si en realidad alimentan a la tabla con datos necesarios o si solo hacen ruido

## Grain
- Es que tanto se expande un dato a trabajar, por ejemplo si es de  mayor amplitud o es algo mas pequeño, ademas de que es necesario saber dicha amplitud para tener un espectro mas preciso a trabajar

## Surrogate Key
- Es una PK alternativa a la que tiene ya de base el dato, para que sea mas facil de ubicar y trabajar, es un numero incrementativo pequeño, en comparacion al tamaño inicial de su id

## SCD
- Es cuando un dato sufre un tipo de cambio y es necesario saber si mantenerlo o sustituirlo por el mas reciente, se debe saber cuando usar cada uno