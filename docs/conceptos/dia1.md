# OLTP vs OLAP
- OLTP: base de datos, se registran datos planos y en una base de datos normalizada en cuanto se realizan transacciones
- OLAP: sirve para analizar multiples tipos de datos que puedan alimentar esa database, desde  distintos angulos y bases de datos, no necesariamente la misma fuente, para tomar  decisiones basadas en esos datos

# ETL vs ELT
- ETL: se trabaja la data antes de subirla al data warehouse o el sistema almacenamiento que se use antes de seguir con su analisis
- ELT: se sube la data tal como viene de su origen, y luego se trabaja con ella dentro del storage que en este caso es cloud, debido a que en la actualidad es mas eficiente en cuanto a costo-produccion

# Batch vs Streaming
- Batch: Se programa una funcion para que se realice a determinados horarios, para tomar la data que se  tenga hasta ese momento y subirlo todo en  conjunto, tal sea que se haya trabajado dicha data o sea todo en raw, la cosa que se sube la data a un tiempo constante   a su respectivo storage
- Streaming: La data se sube de manera constante y a tiempo real, esto sirve mas para tomar decisiones que  se requieran al momento, como tipos de fraudes o sistemas que funcionen con  camapañas al momento

# Data Lake vs Data Warehouse vs Lakehouse
- Data Lake: Aqui se sube la data como viene, se conoce como raw data, sin trabajar y solo como almacenamiento para usar despues, esto se usa por su bajo costo
- Data Warehouse: aqui se sube la data ya trabajada y alineada a lo que se requiera hacer con dicha data
- Lakehouse: se intenta tener un poco de ambos, para conseguir lo mejor de ambos

# Pipelines
- Esto se refiere a la esquematizacion de todo el proceso que debe llevar a cabo la data para poder obtener una data lista para trabajar y tomar acciones con ella.