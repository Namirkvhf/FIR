# Distribución de las plazas FIR

Este proyecto consiste en una representación gráfica de la distribución de las plazas FIR por convocatoria, ciudad y especialidad con un script en Python y un dataset generado a partir de la información de las últimas convocatorias (2016-2019).

El dataset FIR.csv ha sido elaborado a partir de la información de las plazas adjudicadas durante las convocatorias 2016-2019 teniendo en cuenta el número de plaza, la ciudad, la especialidad y el hospital. A partir de éste, se saca la información con la ayuda de un script en python usando la libería pandas y la capacidad de representación gráfica de matplotlib que integra la misma.

El script está diseñado para poder analizar las especialidades y las ciudades disponibles las anteriores convocatorias en función de la plaza obtenida y las ciudades y especialidades deseadas. Para ello, al principio del script se definen las ciudades y especialidades que se desean:
```
ciudades_deseadas = ['MADRID', 'VALENCIA', 'BARCELONA', 'ZARAGOZA']
especialidad = ['FH', 'MICRO','INMUNO', 'AC', 'BQCLIN', 'RAD']
```

Las especialidades son: Farmacia Hospitalaria (FH), Microbiología y Parasitología (MICRO), Inmunología (INMUNO), Análisis Clínicos (AC), Bioquímica Clínica (BQCLIN) y Radiofarmacia (RAD).

Las ciudades disponibles son: MADRID, MURCIA, VALENCIA, SANTIAGO DE COMPOSTELA, ZARAGOZA, BADALONA, PALMA DE MALLORCA, MAJADAHONDA, SEVILLA, PAMPLONA, A CORUNA, BARCELONA, VIGO, BARAKALDO, GRANADA, CADIZ, BILBAO, HOSPITALET, SANTANDER, CARTAGENA, ALBACETE, ALICANTE, OVIEDO, PONTEVEDRA, GETAFE, SALAMANCA, HUELVA, CORDOBA, DONOSTIA, ALCALA DE HENARES, CASTELLON, TOLEDO, MALAGA, FERROL, MATARO, GIJON, VALLADOLID, GUADALAJARA, GIRONA, ESPLUGES DE LLOBREGAT, ELCHE, ALCAZAR DE SAN JUAN, FUENLABRADA, CIUDAD REAL, ALCORCON, LEGANES, SANTA CRUZ DE TENERIFE, AVILES, VITORIA-GASTEIZ, SABADELL, ALZIRA, TERRASSA, SANT JOAN DE ALICANTE, EL EJIDO, OURENSE, BURGOS, LAS PALMAS DE GRAN CANARIA, LEON, GRANOLLERS, TARRAGONA, MARBELLA, JEREZ DE LA FRONTERA, BADAJOZ, JAEN, ORIHUELA, MOSTOLES, LOGRONO, GALDAKAO, SEGOVIA, ALMERIA, PUERTO REAL, LA LAGUNA, CACERES, CUENCA, EIVISSA, LLEIDA, ALGECIRAS, TALAVERA DE LA REINA, IGUALADA, LINARES, ELDA, LUGO, EL FERROL, LA LINEA DE LA CONCEPCION, MERIDA, ALCOY, SANT CUGAT DEL VALLES.

A continuación, se describen las tres distribuciones que se representan:
  - Distribución de plazas por convocatoria en función de la especialidad (sin discriminar ciudades)
  - Distribución de plazas por convocatoria por ciudades deseadas (sin discriminar especialidades)
  - Distribución de plazas por convocatoria, por ciudad y por especialidad (un gráfico por convocatoria/ciudad)

Las siguientes imágenes muestran un ejemplo de los tres tipos de distribuciones en la convocatoria de 2019. El resto se pueden encontrar en la carpeta [Resultados](https://github.com/Namirkvhf/FIR/blob/main/Resultados) o en la carpeta "Resultados pastel" para una paleta de colores con contraste más claro. Por defecto la paleta de colores es la de colores vivos, para cambiarla, hay que modificar la palabra "bright" por "pastel" en todo el código (solo aparece tres veces).

Cada barra en la representación gráfica corresponde a una plaza escogida en ese número para esa Ciudad/Especialidad ese año y cuando no hay barra quiere decir que esa plaza no escogió las ciudades o especialidades escogidas. 


![Imagen 1](https://github.com/Namirkvhf/FIR/blob/main/Resultados/Convocatoria%202019%20por%20especialidades.jpeg)
![Imagen 1](https://github.com/Namirkvhf/FIR/blob/main/Resultados/Plazas%20en%20ciudades%20deseadas%202019.jpeg)
![Imagen 1](https://github.com/Namirkvhf/FIR/blob/main/Resultados/Plazas%20en%20MADRID%202019.jpeg)

En la carpeta [Resultados pastel](https://github.com/Namirkvhf/FIR/blob/main/Resultados%20pastel) se tiene otro contraste de colores como los siguientes:


![Imagen x1](https://github.com/Namirkvhf/FIR/blob/main/Resultados%20pastel/Convocatoria%202019%20por%20especialidades.jpeg)
![Imagen x1](https://github.com/Namirkvhf/FIR/blob/main/Resultados%20pastel/Plazas%20en%20ciudades%20deseadas%202019.jpeg)
![Imagen x1](https://github.com/Namirkvhf/FIR/blob/main/Resultados%20pastel/Plazas%20en%20MADRID%202019.jpeg)
