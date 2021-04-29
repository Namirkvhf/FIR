# Distribución de las plazas FIR

Este proyecto consiste en una representación gráfica de la distribución de las plazas FIR por convocatoria, ciudad y especialidad con un script en Python y un dataset generado a partir de la información de las últimas convocatorias (2016-2019).

El dataset FIR.csv ha sido elaborado a partir de la información de las plazas adjudicadas durante las convocatorias 2016-2019 teniendo en cuenta el número de plaza, la ciudad, la especialidad y el hospital. A partir de éste, se saca la información con la ayuda de un script en python usando la libería pandas y la capacidad de representación gráfica de matplotlib que integra la misma.

El script está diseñado para poder analizar las especialidades y las ciudades disponibles las anteriores convocatorias en función de la plaza obtenida y las ciudades y especialidades deseadas. Para ello, al principio del script se definen las ciudades y especialidades que se desean:
